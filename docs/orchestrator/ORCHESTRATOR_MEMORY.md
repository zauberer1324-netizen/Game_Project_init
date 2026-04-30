# Orchestrator Memory

This file is the Orchestrator's compact operational memory. It helps future
Orchestrator sessions recover project state after long conversations or context
compression.

This file is not the source of truth. Accepted game rules belong in
`CONTEXT.md`. Shared constraints belong in `docs/contracts/`. Durable decisions
belong in `docs/adr/`.

## Current Project Phase

Initial structure and workstream architecture are in place. Game-specific vision
and first prototype direction still need user-guided initialization.

## Current North Star Summary

Not yet defined. Run `orchestrator-init` before starting specialist workstreams.

## Accepted Decision Index

- `docs/adr/0001-separate-operating-framework-from-game-memory.md` - separates
  reusable orchestration framework from game-specific memory.
- `docs/adr/0002-use-workstreams-for-parallel-chat-development.md` - uses scoped
  workstreams and Orchestrator review before central integration.

## Open Questions

- What is the one-sentence game pitch?
- What is the core player fantasy?
- What is the first playable prototype scope?
- Which daily activities are in the first milestone?
- What is the intended progression philosophy for the first playable build?

## Workstreams Ready To Start

None. Run `orchestrator-init` first so all workstreams share the same direction.

## Workstreams Blocked

- `character_design/` - blocked on game vision and art direction.
- `illustration/` - blocked on game vision and art direction.
- `storyline/` - blocked on narrative direction.
- `physics_engine/` - blocked on gameplay contract and target engine.
- `npc_system/` - blocked on narrative and gameplay contracts.
- `ui_hud/` - blocked on gameplay and progression contracts.
- `level_design/` - blocked on game vision, progression, and daily activity
  priorities.
- `progression_system/` - blocked on progression philosophy.
- `daily_activities/*` - blocked on game vision, daily activity priority, and
  progression direction.

## Last Orchestration Action

Added the `workspace-continuity` skill and workflow so Orchestrator and
workstream chats can preserve state before closing, recover from files in new
chats, and survive folder renames, moves, clones, and machine switches. Report:
`docs/reports/workspace-continuity-implementation-report.md`.

## Next Recommended Orchestration Action

Run `orchestrator-init` with the user to define the game's north star, first
prototype scope, initial contracts, and workstream briefs.
