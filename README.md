# STORM Research Skill

A source-grounded, multi-perspective research workflow for AI agents. It combines perspective-guided iterative questioning with explicit counter-evidence, contradiction mapping, auditable process metrics, and conservative knowledge closure.

Version 1.1 replaces automation claims with an executable session contract, deterministic helpers, tests, and safe write defaults.

## What it does

- frames factual, causal, decision, forecast, and normative questions;
- selects explainable perspectives across multiple domains;
- requires opened sources for material factual claims;
- searches for counter-evidence and preserves unresolved contradictions;
- validates a structured research session before synthesis;
- renders durable reports under an authorized `outputs/qa/` directory.

It does not guarantee truth, calibrated confidence, bias-detection accuracy, or complete research coverage.

## Method provenance

The workflow has three distinct layers:

1. **STORM-derived:** diverse perspective discovery, iterative perspective-guided questioning, retrieval grounding, and cited synthesis.
2. **Community workflow:** multi-perspective scan, contradiction map, synthesis, and peer review.
3. **This repository's extensions:** deterministic perspective selection, assertion-level evidence records, counter-evidence gates, auditable coverage metrics, and safe QA-draft closure.

Stanford STORM itself researches and writes Wikipedia-like articles through perspective discovery, simulated source-grounded conversations, outline generation, and article generation. The four-phase workflow in this repository is not the original Stanford architecture. See the [NAACL 2024 paper](https://aclanthology.org/2024.naacl-long.347/) and [official implementation](https://github.com/stanford-oval/storm).

## Repository structure

```text
storm-research/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── adaptive-algorithm.md
│   ├── bias-guardrails.md
│   ├── perspective-library.md
│   ├── perspectives.json
│   ├── theory.md
│   └── tool-recipes.md
├── schemas/session.schema.json
├── scripts/
│   ├── check_links.py
│   ├── render_report.py
│   ├── select_perspectives.py
│   └── validate_session.py
├── templates/
└── tests/
```

## Installation

Install the whole directory so the skill can access its references, scripts, schema, and templates.

```bash
git clone https://github.com/RobinZorro86/storm-research.git
cp -R storm-research "${CODEX_HOME:-$HOME/.codex}/skills/storm-research"
```

For other agent runtimes, place the directory in that runtime's skill location. Map the capability contract in [tool-recipes.md](references/tool-recipes.md) to the tools actually available; tool names are intentionally not hard-coded.

## Usage

Typical requests:

```text
Use storm-research to investigate whether our team should adopt this build system.
Run a multi-perspective analysis of this policy proposal.
Build a contradiction map for the evidence around this claim.
Review this research brief for unsupported claims and missing counter-evidence.
```

Run deterministic perspective selection:

```bash
python3 scripts/select_perspectives.py --domains tech,biz --complexity medium
```

Validate a session and print coverage metrics:

```bash
python3 scripts/validate_session.py tests/fixtures/valid-session.json
```

Render a QA report:

```bash
python3 scripts/render_report.py \
  tests/fixtures/valid-session.json \
  outputs/qa/example-report.md
```

## Safe knowledge closure

The default write target is `outputs/qa/`. The skill does not automatically modify:

- compiled concept pages;
- entity records;
- immutable raw evidence;
- its own perspective or bias rules;
- Git history.

Formal ingestion remains the responsibility of the active knowledge-base workflow and requires its authorization.

## Quality metrics

The validator reports process coverage rather than unsupported accuracy scores:

- claim citation coverage;
- independent corroboration coverage;
- primary-source coverage;
- counter-evidence coverage;
- unresolved-claim rate;
- source-open success rate.

These metrics are diagnostic. They are not calibrated probabilities or proof that a conclusion is correct.

## Development

Requires Python 3.9 or later. Runtime scripts use only the standard library; validation dependencies are used in CI.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_links.py
python3 scripts/validate_session.py tests/fixtures/valid-session.json
```

CI also validates the session fixture against the JSON Schema and checks Skill frontmatter.

## License

MIT License. See [LICENSE](LICENSE).
