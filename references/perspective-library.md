# Perspective catalog

The machine-readable source is [perspectives.json](perspectives.json). This file explains how to interpret and customize it.

## Selection dimensions

Select perspectives from the research need, not role count alone:

1. question type: factual, causal, decision, forecast, or normative;
2. domain: allow multiple weighted domains;
3. stakeholders: beneficiaries, risk bearers, operators, users, and regulators;
4. evidence type: experimental, statistical, documentary, technical, or experiential;
5. useful tension: factual, causal, normative, temporal, or incentive-based.

## Domain catalog

| Domain | Core concerns | Typical perspectives | Useful tension |
|---|---|---|---|
| tech | architecture, security, performance, adoption | architect, security researcher, user, maintainer, skeptic | optimist ↔ skeptic |
| biz | customers, operations, economics, compliance | customer, operator, investor, product, legal | growth ↔ legal |
| sci | validity, statistics, replication, applicability | experimentalist, statistician, peer reviewer, methods scholar | peer review ↔ public simplification |
| soc | affected groups, policy, ethics, history | affected group, policymaker, ethicist, historian | policy intent ↔ lived impact |
| eng | implementation, reliability, support, maintenance | developer, user, SRE, support, project manager | developer quality ↔ delivery pressure |
| phil | assumptions, meaning, systems, practical consequences | skeptic, pragmatist, constructivist, systems thinker | reductionism ↔ systems view |

## Rules

- Include the perspectives needed to expose material uncertainty; do not target a fixed count mechanically.
- Explain why each selected perspective matters to this question.
- Record important excluded perspectives and why they were excluded.
- Add a tension pair only when both sides can produce credible evidence or distinct decision criteria.
- Treat user-supplied perspectives as session-local until repeated use and evaluation justify a catalog change.
- Propose catalog changes in review output; never let a research run edit the catalog automatically.

## Deterministic helper

Run:

```bash
python3 scripts/select_perspectives.py --domains tech,biz --complexity medium
```

The helper returns selected IDs, reasons, and excluded candidates. It is a reproducible starting point, not an oracle.
