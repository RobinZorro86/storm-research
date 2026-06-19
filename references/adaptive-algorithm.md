# Adaptive perspective selection

Use the deterministic helper when reproducibility matters. Override it when the topic requires perspectives not represented in the catalog, but record the reason.

## Inputs

- one or more domains ordered by relevance;
- complexity: simple, medium, or complex;
- optional user-supplied perspective IDs;
- question types and stakeholders from framing.

## Procedure

1. Add the primary domain's core perspectives.
2. Add core perspectives from secondary domains.
3. Add a credible tension pair from the primary domain when space permits.
4. Fill remaining capacity from domain pools in stable order.
5. Append user-supplied perspectives and label them as such.
6. Return selection reasons and excluded candidates.

The helper deliberately uses deterministic ordering. Random sampling makes research runs harder to compare and debug.

## Override conditions

Override the helper when:

- the question is primarily about a named affected group;
- available evidence cannot support a selected role;
- the topic crosses domains whose core perspectives exceed the target size;
- a normative question requires explicit value frameworks;
- a decision question requires operators, users, or risk owners absent from the default set.

Record every override in the session artifact.
