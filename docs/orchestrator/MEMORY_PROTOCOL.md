# Orchestrator Memory Protocol

`ORCHESTRATOR_MEMORY.md` is the Orchestrator's compact recovery file. It helps a
future Orchestrator session recover state after context compression or a new
chat session.

It is not the source of truth. Accepted game rules belong in `CONTEXT.md`.
Shared constraints belong in `docs/contracts/`. Durable decisions belong in
`docs/adr/`.

## Update Triggers

Update or propose an update to `ORCHESTRATOR_MEMORY.md` whenever one of these
events happens:

1. `orchestrator-init` accepts a new game direction.
2. A PRD is created or materially changed.
3. A contract under `docs/contracts/` is created or materially changed.
4. A workstream review accepts, rejects, or sends back proposals.
5. A workstream becomes ready, blocked, or completed.
6. A major open question is answered or added.
7. Approved changes are promoted into `game_project/`.

## Required Sections

The memory file must keep these sections:

- Current Project Phase
- Current North Star Summary
- Accepted Decision Index
- Open Questions
- Workstreams Ready To Start
- Workstreams Blocked
- Last Orchestration Action
- Next Recommended Orchestration Action

## Style Rules

- Keep it compact.
- Link to source files instead of copying long content.
- Do not turn assumptions into accepted decisions.
- Do not store raw workstream notes here.
- Do not use this file as a replacement for PRDs, contracts, ADRs, or reports.

## Freshness Check

Run this check before starting a new Orchestrator session or before merging a
workstream:

```powershell
$env:PYTHON_BIN = "path-to-python-if-needed"
python .\scripts\check_memory_freshness.py
```

If the check reports newer handoffs, PRDs, ADRs, or reports, update the memory
or intentionally explain why it does not need an update.
