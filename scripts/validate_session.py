#!/usr/bin/env python3
"""Validate the research gates and print auditable coverage metrics."""

import argparse
import json
from pathlib import Path

FINAL_PHASES = {"synthesis", "review", "qa"}
PHASES = {"framing", "scan", "contradiction", "synthesis", "review", "qa"}
QUESTION_TYPES = {"factual", "causal", "decision", "forecast", "normative"}
CLAIM_FIELDS = {"id", "text", "kind", "impact", "status", "sources", "counter_evidence"}
SOURCE_FIELDS = {"url", "title", "source_type", "independence_group", "opened", "supports_claim"}


def ratio(numerator, denominator):
    return round(numerator / denominator, 3) if denominator else None


def validate(session):
    errors = []
    for field in ("topic", "question_types", "phase", "perspectives", "claims"):
        if field not in session:
            errors.append(f"session: missing required field {field}")
    question_types = session.get("question_types", [])
    if not question_types or any(item not in QUESTION_TYPES for item in question_types):
        errors.append("session: question_types must contain supported values")
    if session.get("phase") not in PHASES:
        errors.append("session: phase is invalid")
    if not isinstance(session.get("perspectives", []), list) or not isinstance(session.get("claims", []), list):
        errors.append("session: perspectives and claims must be arrays")
        return errors, {}
    claims = session.get("claims", [])
    factual = [claim for claim in claims if claim.get("kind") == "factual"]
    high_impact = [claim for claim in factual if claim.get("impact") == "high"]

    for claim in claims:
        claim_id = claim.get("id", "<missing-id>")
        missing_claim_fields = CLAIM_FIELDS - set(claim)
        if missing_claim_fields:
            errors.append(f"{claim_id}: missing fields {', '.join(sorted(missing_claim_fields))}")
        sources = claim.get("sources", [])
        for index, source in enumerate(sources):
            missing_source_fields = SOURCE_FIELDS - set(source)
            if missing_source_fields:
                errors.append(f"{claim_id}: source {index} missing fields {', '.join(sorted(missing_source_fields))}")
            if not str(source.get("url", "")).startswith(("http://", "https://")):
                errors.append(f"{claim_id}: source {index} URL must use http or https")
        supporting = [source for source in sources if source.get("opened") and source.get("supports_claim")]
        if session.get("phase") in FINAL_PHASES and claim.get("kind") == "factual" and not supporting:
            errors.append(f"{claim_id}: final-phase factual claim has no opened supporting source")
        if claim.get("status") == "verified" and not supporting:
            errors.append(f"{claim_id}: verified claim has no opened supporting source")
        if claim.get("impact") == "high" and claim.get("kind") == "factual" and not claim.get("counter_evidence"):
            errors.append(f"{claim_id}: high-impact factual claim has no counter-evidence search record")

    cited = sum(any(source.get("opened") and source.get("supports_claim") for source in claim.get("sources", [])) for claim in factual)
    corroborated = 0
    primary = 0
    opened_sources = 0
    all_sources = []
    for claim in factual:
        sources = claim.get("sources", [])
        all_sources.extend(sources)
        independent = {source.get("independence_group") for source in sources if source.get("opened") and source.get("supports_claim")}
        corroborated += len(independent - {None, ""}) >= 2
        primary += any(source.get("opened") and source.get("primary") and source.get("supports_claim") for source in sources)
    for source in all_sources:
        opened_sources += bool(source.get("opened"))

    metrics = {
        "claim_citation_coverage": ratio(cited, len(factual)),
        "independent_corroboration_coverage": ratio(corroborated, len(high_impact)),
        "primary_source_coverage": ratio(primary, len(factual)),
        "counter_evidence_coverage": ratio(sum(bool(c.get("counter_evidence")) for c in high_impact), len(high_impact)),
        "unresolved_claim_rate": ratio(sum(c.get("status") == "unresolved" for c in claims), len(claims)),
        "source_open_success": ratio(opened_sources, len(all_sources)),
    }
    return errors, metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("session")
    args = parser.parse_args()
    session = json.loads(Path(args.session).read_text(encoding="utf-8"))
    errors, metrics = validate(session)
    print(json.dumps({"valid": not errors, "errors": errors, "metrics": metrics}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
