#!/usr/bin/env python3
"""Render a session as a conservative QA report."""

import argparse
import json
from pathlib import Path

try:
    from scripts.validate_session import validate
except ModuleNotFoundError:
    from validate_session import validate


def render(session):
    lines = [f"# {session['topic']}", "", "## Answer", "", session.get("summary", "No synthesis recorded."), ""]
    lines.extend(["## Claims", ""])
    for claim in session.get("claims", []):
        lines.append(f"### {claim['id']}: {claim['text']}")
        lines.append("")
        lines.append(f"Status: `{claim['status']}`; evidence strength: `{claim.get('evidence_strength', 'none')}`.")
        lines.append("")
        for source in claim.get("sources", []):
            lines.append(f"- [{source['title']}]({source['url']}) — {source['source_type']}")
        if claim.get("counter_evidence"):
            lines.append("")
            lines.append("Counter-evidence:")
            lines.extend(f"- {item}" for item in claim["counter_evidence"])
        lines.append("")
    lines.extend(["## Implications", ""])
    lines.extend(f"- {item}" for item in session.get("implications", []))
    lines.extend(["", "## Open questions", ""])
    lines.extend(f"- {item}" for item in session.get("open_questions", []))
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("session")
    parser.add_argument("output")
    args = parser.parse_args()
    output = Path(args.output)
    parts = output.resolve().parts
    if not any(parts[index:index + 2] == ("outputs", "qa") for index in range(len(parts) - 1)):
        parser.error("output must be under an outputs/qa directory")
    session = json.loads(Path(args.session).read_text(encoding="utf-8"))
    errors, _ = validate(session)
    if errors:
        raise SystemExit("Session validation failed:\n" + "\n".join(errors))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(session), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
