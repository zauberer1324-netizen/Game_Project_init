# Data Analysis Workflow

Use this workflow for evidence-heavy factual questions, medical or scientific
claims, market research, policy checks, and questions where recency matters.

## Steps

1. Classify risk.
2. Select accuracy rules and strict-review skill.
3. Collect raw sources into `data/raw/`.
4. Extract atomic facts into `data/extracted/`.
5. Verify facts against source locations.
6. Detect conflicts and preserve them.
7. Create an evidence table.
8. Create a conflict table when needed.
9. Run strict review.
10. Produce final answer with facts, inferences, limits, and recommendations.

## Required Evidence Fields

- `source_id`
- `source_type`
- `title`
- `url` or `raw_path`
- `retrieved_at`
- `location`
- `confidence`

## Final Output Additions

- Evidence Table
- Conflict Table
- Calculation Log, if calculations were used
- Strict Review Result

