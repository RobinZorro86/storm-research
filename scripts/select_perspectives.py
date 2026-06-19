#!/usr/bin/env python3
"""Select a deterministic, explainable perspective set."""

import argparse
import json
from pathlib import Path

SIZE = {"simple": 3, "medium": 5, "complex": 7}


def load_library():
    path = Path(__file__).resolve().parents[1] / "references" / "perspectives.json"
    return json.loads(path.read_text(encoding="utf-8"))


def select(domains, complexity, custom=None):
    library = load_library()
    if not domains:
        raise ValueError("at least one domain is required")
    if complexity not in SIZE:
        raise ValueError(f"unknown complexity: {complexity}")
    unknown = [domain for domain in domains if domain not in library]
    if unknown:
        raise ValueError(f"unknown domain(s): {', '.join(unknown)}")

    target = SIZE[complexity]
    candidates = []
    reasons = {}
    primary = domains[0]
    for item in library[primary]["core"]:
        if item not in candidates:
            candidates.append(item)
            reasons[item] = f"core perspective for {primary}"
    for domain in domains[1:]:
        for item in library[domain]["core"][:1]:
            if item not in candidates:
                candidates.append(item)
                reasons[item] = f"core perspective for {domain}"
    for pair in library[primary]["tension_pairs"]:
        for item in pair:
            if item not in candidates:
                candidates.append(item)
                reasons[item] = f"tension perspective for {primary}"
    for domain in domains:
        for item in library[domain]["core"] + library[domain]["pool"]:
            if item not in candidates:
                candidates.append(item)
                reasons[item] = f"supporting perspective for {domain}"

    selected = candidates[:target]
    for item in custom or []:
        if item and item not in selected:
            selected.append(item)
            reasons[item] = "user-supplied perspective"

    return {
        "domains": domains,
        "complexity": complexity,
        "selected": [{"id": item, "reason": reasons[item]} for item in selected],
        "excluded": candidates[target:],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domains", required=True, help="comma-separated domain ids")
    parser.add_argument("--complexity", choices=SIZE, default="medium")
    parser.add_argument("--custom", default="", help="comma-separated custom perspective ids")
    args = parser.parse_args()
    domains = [item.strip() for item in args.domains.split(",") if item.strip()]
    custom = [item.strip() for item in args.custom.split(",") if item.strip()]
    try:
        result = select(domains, args.complexity, custom)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
