---
name: strict-review
description: Reviews final answers, reports, extracted facts, calculations, and evidence tables for unsupported claims, stale sources, hidden conflicts, overstatement, and schema violations. Use for evidence-heavy, medical, legal, financial, scientific, high-risk, or user-facing final answers.
---

# Strict Review

## Role

Act as the final accuracy reviewer before delivery.

## Required Checks

1. Every factual claim has evidence.
2. Every evidence item has `source_id`, `location`, `retrieved_at`, and
   `confidence`.
3. Search snippets are not used as evidence.
4. Inferences are labeled separately from facts.
5. Conflicts are preserved and disclosed.
6. Dates are concrete where recency matters.
7. Calculations are reproducible.
8. The conclusion is no stronger than the evidence allows.
9. Unsupported claims are removed or marked `UNVERIFIED`.
10. Output matches the required schema.

## Output

Return only:

```json
{
  "pass": true,
  "risk_level": "low",
  "issues": [],
  "required_fixes": [],
  "unsupported_claims": [],
  "conflicts_missed": [],
  "final_recommendation": "approve"
}
```

