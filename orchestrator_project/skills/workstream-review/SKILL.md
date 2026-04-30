---
name: workstream-review
description: Reviews one or more workstream outputs before central integration. Checks HANDOFF files, proposed context updates, proposed ADRs, contracts, vision fit, conflicts, and implementation risks. Use when a workstream finishes, before merging workstream results, or when the Orchestrator needs to decide what becomes project memory or game_project changes.
---

# Workstream Review

## Role

Act as the Orchestrator merge gate for workstream outputs.

## Goal

Decide what can be accepted, what needs revision, and what must be rejected
before updating central project memory or implementation.

## Source Of Truth Rules

- `CONTEXT.md` is accepted game memory.
- `docs/contracts/*` are accepted shared constraints.
- `docs/orchestrator/ORCHESTRATOR_MEMORY.md` is the Orchestrator's operational
  status board, not the final source of truth.
- Workstream files are proposals until reviewed and accepted.

## Process

### 1. Identify Scope

Confirm:

- Which workstream(s) are being reviewed
- Whether this is design review, contract review, implementation review, or
  final merge review
- Whether the user wants review only or review plus file edits after approval

### 2. Read In Order

Read:

1. `AGENTS.md`
2. `CONTEXT.md`
3. `docs/orchestrator/ORCHESTRATOR_MEMORY.md` if it exists
4. Relevant `docs/contracts/*`
5. `workstreams/<name>/BRIEF.md`
6. `workstreams/<name>/HANDOFF.md`
7. `workstreams/<name>/proposed_context_updates.md`
8. `workstreams/<name>/proposed_adr.md`

Only read `OUTPUT.md`, `artifacts/`, `tests/`, or `notes/` if the handoff is
unclear or a conflict requires more detail.

### 3. Vision-Fit Checkpoint

Before doing the full review, check whether the proposal appears aligned with:

- `docs/contracts/game_vision.md`
- accepted direction in `CONTEXT.md`
- current north star in `docs/orchestrator/ORCHESTRATOR_MEMORY.md`, if present

If you believe a proposal does not fit the game vision, do not immediately
reject it. First write a user-facing note:

```text
Vision Fit Concern

I think this proposal may not fit the current game vision because:
- reason 1
- reason 2
- reason 3

Possible ways to handle it:
1. Reject this direction.
2. Revise the proposal to fit the current vision.
3. Reopen the game vision and intentionally change the direction.
4. Treat it as an alternate concept for later.

Please choose how you want me to review the rest of this workstream.
```

Wait for the user's direction before continuing the subjective vision review.

### 4. Direct Technical And Structural Checks

For non-subjective issues, make the call directly. Do not block on the user for
clear mechanical problems.

Directly identify and classify:

- Missing required files
- Broken handoff format
- Contradictions with explicit contracts
- Duplicate ownership between workstreams
- Attempts to directly modify forbidden central files
- Code interface conflicts
- Asset pipeline conflicts
- Daily activity ownership conflicts
- Proficiency formula ownership conflicts
- Level design trying to own XP curves
- Physical file conflicts or merge risks
- Test or verification gaps

### 5. Proposal Review Table

Classify every proposal:

| Proposal | Source | Decision | Reason | Required Action |
| --- | --- | --- | --- | --- |
| ... | ... | accept / revise / reject / user-decision-needed | ... | ... |

Use `user-decision-needed` only for subjective direction choices, product taste,
or intentional vision changes.

### 6. Conflict Table

List conflicts separately:

| Conflict | Sources | Why It Matters | Resolution |
| --- | --- | --- | --- |

For mechanical or contract conflicts, recommend a resolution. For vision
conflicts, use the Vision-Fit Checkpoint process.

### 7. Integration Plan

If anything is accepted, propose exact updates for:

- `CONTEXT.md`
- `docs/contracts/*`
- `docs/adr/*`
- `docs/issues/*`
- `docs/reports/*`
- `docs/orchestrator/ORCHESTRATOR_MEMORY.md`
- `game_project/*`

Do not edit until the user confirms.

### 8. Orchestrator Memory Update

After review, update or propose updates to
`docs/orchestrator/ORCHESTRATOR_MEMORY.md` with:

- Workstreams reviewed
- Accepted proposals
- Rejected proposals
- Revision requests
- Vision concerns waiting on the user
- New open questions
- Next integration step
- Links to generated reports

Keep this compact. Link to detailed reports instead of copying them.

### 9. Report

Write or propose a report under:

`docs/reports/<workstream>-review.md`

The report should include:

- Scope
- Files reviewed
- Vision-fit result
- Accepted items
- Items needing revision
- Rejected items
- Conflicts
- Integration plan
- Orchestrator memory update

## Completion Criteria

Done when every proposal is accepted, rejected, sent back for revision, or marked
as waiting on user direction.
