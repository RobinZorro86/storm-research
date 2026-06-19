#!/usr/bin/env python3
"""Fail when a local Markdown resource link points to a missing file."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
missing = []
for document in ROOT.rglob("*.md"):
    text = document.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^]]+\]\(([^)#]+)(?:#[^)]+)?\)", text):
        if "://" in target or target.startswith("mailto:"):
            continue
        path = (document.parent / target).resolve()
        if not path.exists():
            missing.append(f"{document.relative_to(ROOT)} -> {target}")
if missing:
    raise SystemExit("Missing local links:\n" + "\n".join(missing))
print("All local Markdown links resolve.")
