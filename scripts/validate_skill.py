#!/usr/bin/env python3
"""Validate the minimal SKILL.md frontmatter contract."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
if not match:
    raise SystemExit("SKILL.md has no valid YAML frontmatter")
frontmatter = {}
for line in match.group(1).splitlines():
    key, separator, value = line.partition(":")
    if not separator:
        raise SystemExit(f"Invalid frontmatter line: {line}")
    frontmatter[key.strip()] = value.strip().strip('"')
if set(frontmatter) != {"name", "description"}:
    raise SystemExit("SKILL.md frontmatter must contain only name and description")
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", frontmatter["name"]):
    raise SystemExit("Skill name must use lowercase hyphen-case")
if not frontmatter["description"].strip():
    raise SystemExit("Skill description must be a non-empty string")
print("Skill frontmatter is valid.")
