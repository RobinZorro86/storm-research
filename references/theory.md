# Method provenance and boundaries

## Three-layer provenance

Do not present the entire workflow as Stanford STORM.

### 1. STORM-derived mechanisms

The 2024 Stanford OVAL system researches and writes Wikipedia-like articles by:

1. discovering diverse perspectives from related material;
2. simulating conversations in which perspective-conditioned writers ask a source-grounded expert iterative follow-up questions;
3. curating the collected information into an outline;
4. generating and polishing a cited article.

The transferable mechanism used by this skill is perspective-guided, iterative questioning grounded in retrieved sources. The reported 25-point organization and 10-point coverage improvements compare STORM with an outline-driven retrieval baseline in the paper's evaluation; they are not general accuracy guarantees.

Primary sources:

- [NAACL 2024 paper](https://aclanthology.org/2024.naacl-long.347/)
- [Stanford OVAL implementation](https://github.com/stanford-oval/storm)

### 2. Community workflow

The sequence “multi-perspective scan → contradiction map → synthesis → peer review” is a community adaptation recorded in the author's knowledge base. It is useful scaffolding, but it is not the architecture evaluated in the Stanford paper.

### 3. storm-research extensions

This repository adds:

- deterministic perspective selection and explicit tension pairs;
- assertion-level evidence records;
- counter-evidence search and layered contradiction mapping;
- auditable coverage metrics;
- conservative QA-draft knowledge closure.

These extensions are hypotheses to test through forward evaluation. Do not claim that they improve accuracy until benchmark evidence exists.

## Design principles

- Evidence quality matters more than the number of perspectives.
- Useful tension can be factual, causal, normative, stakeholder-based, or temporal.
- The system must not manufacture disagreement when sources converge.
- A structured session is the source of truth; prose reports are rendered views.
- Self-review supplements deterministic validation but does not replace independent review.
- Knowledge-base writes follow the active repository's governance rules.

## Known limitations

- Retrieval can transfer source bias and omit long-tail evidence.
- Multiple perspectives can create false balance.
- Same-model review is correlated with generation errors.
- Coverage metrics measure process compliance, not truth.
- Public evidence may be insufficient for private, emerging, or high-stakes questions.
