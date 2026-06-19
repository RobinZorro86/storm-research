# Evidence and red-team rubric

## Assertion gate

For every material factual claim, record:

- exact claim text;
- impact: high, medium, or low;
- opened source URL and title;
- source type and independence group;
- whether the source is primary;
- whether the source actually supports the claim;
- status: verified, unresolved, or rejected;
- evidence strength: strong, moderate, weak, or none.

Do not use numeric confidence as if it were a calibrated probability.

## Source hierarchy

Prefer evidence in this order when it exists:

1. original paper, dataset, specification, law, filing, source code, or first-party documentation;
2. independent replication, audit, benchmark, or systematic review;
3. reputable secondary analysis with transparent methods;
4. expert commentary with disclosed identity and incentives;
5. social or community anecdotes for hypothesis generation only.

Source type is not an automatic truth score. Check method quality, applicability, independence, date, and conflicts of interest.

## Counter-evidence protocol

For each high-impact factual claim:

1. State what observation would falsify or materially narrow it.
2. Search for criticism, failed replication, contrary data, boundary conditions, and alternative causal explanations.
3. Open the strongest counter-source.
4. Record whether it rejects, narrows, or does not affect the claim.
5. Leave the claim unresolved when the conflict cannot be adjudicated.

Do not create a weak opponent merely to satisfy a quota.

## Bias checks

- source concentration: several citations trace to the same organization or dataset;
- confirmation bias: supportive queries greatly outnumber falsification queries;
- false balance: fringe disagreement is presented as equal to convergent evidence;
- survivorship bias: only successful examples are visible;
- framing bias: the question excludes affected stakeholders or alternative outcomes;
- recency bias: new sources displace stronger older evidence without reason;
- authority bias: reputation substitutes for methods;
- social amplification: popularity is treated as representativeness;
- citation laundering: secondary sources are cited instead of the underlying evidence;
- over-association: related facts are combined into an unsupported causal story.

## Auditable metrics

Measure process coverage only:

- claim citation coverage;
- independent corroboration coverage for high-impact factual claims;
- primary-source coverage;
- counter-evidence coverage;
- unresolved-claim rate;
- source-open success rate.

These metrics do not measure truth, bias-detection accuracy, or research completeness. Such claims require a labeled benchmark and external evaluation.
