# Orchestrator Init Workflow

Use this workflow before specialist workstreams begin.

## Steps

1. Read project memory, Orchestrator memory, startup criteria, and engine profile index.
2. Run a one-question-at-a-time alignment interview.
3. Separate accepted decisions, assumptions, open questions, and later decisions.
4. Decide the engine status:
   - selected engine and matching `engine_profiles/*.md`, or
   - deferred engine decision with reason and affected blocked workstreams.
5. If an engine is selected, propose profile attachment, code-interface contract updates, and an engine-selection ADR.
6. Propose updates for context, contracts, first PRD, workstream briefs, and Orchestrator memory.
7. Show planned file changes before editing.
8. Update files only after user confirmation.

## Output

- Direction summary
- Engine status: selected or deferred with reason
- Open questions
- Proposed context and contract updates
- Proposed first PRD
- Proposed engine-selection ADR when applicable
- Proposed memory updates
- Workstream readiness status
- Next recommended action
