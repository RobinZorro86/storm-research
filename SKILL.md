---
name: storm-research
description: "Run source-grounded, multi-perspective research with explicit counter-evidence, contradiction mapping, synthesis, and review. Use when the user asks for STORM research, multi-perspective analysis, a contradiction map, a research brief, or a source-audited investigation."
---

# STORM Research

Treat this skill as a research workflow, not as a promise of autonomous truth finding. Separate the parts derived from Stanford STORM from this skill's extensions; read [theory.md](references/theory.md) when explaining the methodology.

## Operating contract

1. Preserve a structured session artifact throughout the run. Use [session.schema.json](schemas/session.schema.json) as the data contract.
2. Cite factual claims at assertion level. A search-result snippet is discovery material, not evidence; open the source before citing it.
3. Prefer primary sources. Record source type, independence group, publication date when known, and whether the source is primary.
4. Search for counter-evidence for high-impact factual claims. Keep unresolved claims visible rather than forcing a conclusion.
5. Treat `evidence_strength` as a review label, never as a calibrated probability.
6. Default knowledge closure to a QA draft under `outputs/qa/`. Do not edit `concepts/`, `entities/`, `raw/`, the skill itself, or Git history unless the user's repository rules explicitly authorize it.
7. Never describe an unavailable or skipped tool call as completed.

## Workflow

### 1. Frame the question

- Restate the research question, decision it informs, time horizon, geography, and exclusions.
- Classify the question as one or more of: factual, causal, decision, forecast, normative.
- Ask only when a missing choice would materially change the research.

### 2. Select perspectives

- Infer one or more weighted domains instead of forcing a single domain.
- Select perspectives based on question type, stakeholders, evidence types, and useful tension.
- Explain why each perspective was selected and note important excluded candidates.
- Use `python3 scripts/select_perspectives.py --domains <comma-separated> --complexity <simple|medium|complex>` when deterministic selection is useful.
- Read [perspective-library.md](references/perspective-library.md) only when custom selection or interpretation is needed.

### 3. Retrieve and interrogate evidence

- Read relevant local knowledge indexes before specific notes when a knowledge base is in scope.
- Run broad discovery queries, then open authoritative sources.
- For each perspective, ask follow-up questions that expose missing mechanisms, boundary conditions, incentives, and failure cases. This iterative questioning is the main STORM-derived mechanism.
- Capture claims and sources in the session artifact as research proceeds.
- Follow the platform-neutral tool contract in [tool-recipes.md](references/tool-recipes.md).

### 4. Build the contradiction map

- Separate factual contradictions, explanatory disagreements, and value conflicts.
- Search for the strongest counter-evidence to each high-impact factual claim.
- Do not manufacture disagreement when evidence converges.
- Mark each claim `verified`, `unresolved`, or `rejected` and preserve competing explanations.
- Use [contradiction-map.md](templates/contradiction-map.md) for presentation and [bias-guardrails.md](references/bias-guardrails.md) for source and bias checks.

### 5. Synthesize

- Lead with the answer and its decision implications.
- Distinguish established findings, plausible interpretations, value judgments, and open questions.
- Cite every material factual claim near the claim.
- Include the strongest contrary evidence and explain what would change the conclusion.
- Use [synthesis-report.md](templates/synthesis-report.md) when a standalone report is requested.

### 6. Review and close safely

- Run `python3 scripts/validate_session.py <session.json>` before finalizing.
- Complete [peer-review-checklist.md](templates/peer-review-checklist.md).
- Prefer an independent review context when available; provide only the report, evidence package, and rubric.
- Render a durable QA draft with `python3 scripts/render_report.py <session.json> <path-under-outputs/qa.md>`.
- Show the proposed write target and obtain any confirmation required by the active repository or knowledge-base rules.

## Stop and degrade safely

- If browsing or source-opening tools are unavailable, state that the output is a hypothesis map rather than completed research.
- If a high-impact claim lacks an opened source, keep it unresolved and exclude it from the decisive conclusion.
- If local knowledge conflicts with stronger new evidence, report the conflict; do not overwrite existing truth records automatically.
- For medical, legal, financial, or other high-stakes topics, provide research context only and require appropriate expert review.

## Quality gates

Report auditable coverage metrics rather than unsupported accuracy claims:

- claim citation coverage
- independent corroboration coverage for high-impact factual claims
- primary-source coverage when primary sources are available
- counter-evidence coverage for high-impact factual claims
- unresolved-claim rate
- source-open success rate

Do not claim a bias-detection percentage, conflict-detection percentage, or calibrated confidence score without a labeled evaluation set.

## Resources

- [theory.md](references/theory.md): provenance and methodological boundaries
- [adaptive-algorithm.md](references/adaptive-algorithm.md): perspective-selection rules
- [perspective-library.md](references/perspective-library.md): human-readable perspective catalog
- [bias-guardrails.md](references/bias-guardrails.md): evidence and red-team rubric
- [tool-recipes.md](references/tool-recipes.md): runtime-neutral tool adapters
- [storm-session.md](templates/storm-session.md): human-readable session view
- [concept-output.md](templates/concept-output.md): optional Hermes ingestion candidate, never the default write target
