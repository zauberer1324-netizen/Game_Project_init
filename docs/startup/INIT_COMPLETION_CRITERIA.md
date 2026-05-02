# Orchestrator Init Completion Criteria

`orchestrator-init` is complete only when the Orchestrator can clearly answer:

1. What game are we making?
2. What is the player's core fantasy?
3. What is the first playable prototype?
4. What should not be built yet?
5. Which contracts contain accepted decisions?
6. Which workstreams can start now?
7. Which workstreams are blocked, and why?
8. Which engine profile is selected, or why engine selection is deferred?
9. What should the next Orchestrator action be?

## Required File State

- `CONTEXT.md` has game-specific accepted language or decisions.
- `docs/contracts/game_vision.md` has a real direction.
- `docs/contracts/gameplay_contract.md` has enough rules for prototype planning.
- `docs/prd/prototype-1.md` exists or an equivalent first PRD exists.
- `docs/orchestrator/ORCHESTRATOR_MEMORY.md` has a current north star summary.
- `docs/orchestrator/ORCHESTRATOR_MEMORY.md` has a `Selected Engine` section.
- Relevant `workstreams/*/BRIEF.md` files are ready or explicitly blocked.

## Engine Status Requirement

The engine decision may be selected or deferred, but it must not be missing.

| Engine Status | Required Record | Expected Follow-Up |
| --- | --- | --- |
| Selected | Engine name, profile path, and decision source | Draft engine-selection ADR, update `code_interface_contract.md`, and attach the profile when approved. |
| Deferred | Reason, decision owner, and revisit trigger | Mark engine-dependent workstreams blocked until the trigger is resolved. |

Engine-dependent workstreams usually include `physics_engine`, `ui_hud`,
`game_sound`, and any implementation work under `game_project/`.

## Not Required

- Final lore bible
- Final art bible
- Final engine architecture
- Full feature list
- Complete balance tables
- Production-ready code
## Optional Strict Check

After the user confirms that initialization is complete, the Orchestrator may
run:

```powershell
python .\scripts\check_init_completion.py
```

This check is intentionally not part of the default quality gate because a fresh
workspace is expected to fail it before `orchestrator-init` runs.
