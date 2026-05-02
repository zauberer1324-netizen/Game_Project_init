# Orchestrator Memory

This file is the Orchestrator's compact operational memory. It helps future
Orchestrator sessions recover project state after long conversations or context
compression.

This file is not the source of truth. Accepted game rules belong in
`CONTEXT.md`. Shared constraints belong in `docs/contracts/`. Durable decisions
belong in `docs/adr/`.

## Current Project Phase

Initial structure, workstream architecture, workspace continuity, workspace
guard, Project Architect role support, and audio workstream scaffolding are in
place. Game-specific vision and first prototype direction still need
user-guided initialization.

## Current North Star Summary

Not yet defined. Run `orchestrator-init` before starting specialist workstreams.

## Accepted Decision Index

- `docs/adr/0001-separate-operating-framework-from-game-memory.md` - separates
  reusable orchestration framework from game-specific memory.
- `docs/adr/0002-use-workstreams-for-parallel-chat-development.md` - uses scoped
  workstreams and Orchestrator review before central integration.
- `docs/reports/workspace-continuity-implementation-report.md` - adds recovery
  workflow for folder renames, machine switches, and new chat sessions.
- `docs/reports/workspace-guard-implementation-report.md` - adds optional
  read-only workspace mode guards without ACL hard locks.
- `docs/reports/project-architect-implementation-report.md` - adds Project
  Architect as a workspace-structure role separate from Orchestrator and game
  development authority.
- `docs/reports/audio-workstream-architecture-report.md` - adds proposal-only
  `bgm/` and `game_sound/` workstreams plus the central `audio_contract.md`.

## Open Questions

- What is the one-sentence game pitch?
- What is the core player fantasy?
- What is the first playable prototype scope?
- Which daily activities are in the first milestone?
- What is the intended progression philosophy for the first playable build?
- What is the first prototype's audio priority: BGM mood, gameplay feedback,
  ambience, UI clarity, or silence-first implementation?

## Workstreams Ready To Start

None. Run `orchestrator-init` first so all workstreams share the same direction.

## Workstreams Blocked

- `character_design/` - blocked on game vision and art direction.
- `illustration/` - blocked on game vision and art direction.
- `storyline/` - blocked on narrative direction.
- `bgm/` - blocked on game vision, narrative tone, audio direction, and asset
  provenance rules.
- `game_sound/` - blocked on game vision, gameplay contract, audio direction,
  code interface expectations, and first prototype scope.
- `physics_engine/` - blocked on gameplay contract and target engine.
- `npc_system/` - blocked on narrative and gameplay contracts.
- `ui_hud/` - blocked on gameplay and progression contracts.
- `level_design/` - blocked on game vision, progression, and daily activity
  priorities.
- `progression_system/` - blocked on progression philosophy.
- `daily_activities/*` - blocked on game vision, daily activity priority, and
  progression direction.

## Last Orchestration Action

Added audio workstream scaffolding. The template now includes `bgm/` and
`game_sound/` proposal workstreams, `audio_contract.md`, audio dependency
mappings, generated start prompts, and an audio architecture report.
Report: `docs/reports/audio-workstream-architecture-report.md`.

## Next Recommended Orchestration Action

For game-start work in this Orchestrator chat, run `orchestrator-init` with
the user to define the game's north star, first prototype scope, initial
contracts, and workstream briefs.

If the user asks for workspace-structure changes such as folders, skills,
workflows, routers, guardrails, or workstream scaffolds, do not handle that
request as the Orchestrator. Ask the user to open or switch to a separate
Project Architect chat and run Project Architect init there.
