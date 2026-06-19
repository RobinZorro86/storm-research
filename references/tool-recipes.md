# Runtime-neutral tool contract

Use capabilities, not hard-coded product-specific tool names. Map each capability to the active runtime before starting.

| Capability | Required behavior | Safe degradation |
|---|---|---|
| local read | Read indexes first, then relevant files | Ask for supplied context |
| local search | Find relevant files or passages without scanning prohibited areas | Use index links only |
| web discovery | Find candidate sources and opposing evidence | Mark research incomplete |
| source open | Open the original page, paper, dataset, or documentation | Do not cite snippets as evidence |
| durable write | Write only to an authorized QA/notes location | Return report in chat |
| user confirmation | Pause before governed or external mutations | Keep a preview only |

## Phase 1: framing and knowledge preflight

1. Parse the topic, decision, time horizon, geography, and exclusions.
2. Read the knowledge-base indexes required by local instructions.
3. Resolve only the relevant concept and entity files.
4. Never read prohibited source directories merely because a search matched them.

Output: scope, question types, known baseline, and open uncertainties.

## Phase 2: perspective-guided retrieval

1. Select perspectives with `scripts/select_perspectives.py` or explain a custom set.
2. Run broad discovery queries for the topic and primary sources.
3. Open candidate sources before creating evidence records.
4. For each perspective, ask iterative follow-up questions about mechanisms, boundaries, incentives, affected stakeholders, failure cases, and missing evidence.
5. Record each factual claim and source in the session artifact.

Output: perspective cards, claims, opened sources, and unanswered questions.

## Phase 3: contradiction and counter-evidence

1. Prioritize high-impact factual claims.
2. Search for counter-evidence and failed replications; open the strongest candidates.
3. Separate factual contradictions, explanatory disagreements, and value conflicts.
4. Compare new claims with the loaded knowledge baseline without modifying it.
5. Keep unresolved conflicts explicit.

Output: contradiction map and updated claim statuses.

## Phase 4: synthesis and review

1. Synthesize from the structured session, not from memory alone.
2. Put decisive contrary evidence next to the conclusion it challenges.
3. Run `scripts/validate_session.py`.
4. Run the peer-review checklist in a fresh context when available.
5. Re-open any source whose support for a decisive claim is ambiguous.

Output: reviewed report and audit metrics.

## Phase 5: safe closure

1. Render the report under an authorized `outputs/qa/` location.
2. Show the exact paths to be written.
3. Do not write `concepts/`, `entities/`, `raw/`, modify the skill, or commit Git unless active instructions explicitly allow those actions.
4. If formal ingestion is requested, create an ingestion candidate and hand it to the designated knowledge maintainer.

Output: QA report plus a concise read/write manifest.
