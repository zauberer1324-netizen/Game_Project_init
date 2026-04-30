# New Game Start Checklist

Use this checklist before opening specialist workstream chats.

## Required First Step

Run the `orchestrator-init` workflow with the user. Do not start serious
workstream production before the game's first direction is accepted.

## Minimum Direction

- One-sentence game pitch
- Core player fantasy
- Primary loop
- Secondary loops
- Genre
- Camera or perspective
- Target platform
- Session length expectation
- First 10 minutes of play
- First playable prototype scope
- Explicit out-of-scope items

## Minimum Contracts

These contracts should contain game-specific decisions, not only template text:

- `docs/contracts/game_vision.md`
- `docs/contracts/gameplay_contract.md`
- `docs/contracts/art_direction.md` if visual work starts early
- `docs/contracts/narrative_contract.md` if story or NPC work starts early
- `docs/contracts/progression_contract.md` if daily activities or long-term growth starts early
- `docs/contracts/code_interface_contract.md` before parallel implementation work

## Minimum Planning Artifacts

- At least one PRD under `docs/prd/`
- Workstreams marked ready or blocked in `docs/orchestrator/ORCHESTRATOR_MEMORY.md`
- Relevant `workstreams/*/BRIEF.md` files updated for the first milestone
- Open questions recorded

## Quality Gate

Run:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1
```

The project is ready for parallel workstreams only after the quality gate passes
and the Orchestrator memory states which workstreams are ready.
