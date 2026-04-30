# Multi-Workstream Game Development Orchestration Blueprint

This blueprint defines how separate AI chat sessions can work on different parts
of the same game without polluting the main project memory or overflowing the
Orchestrator context window.

## Core Decision

Use `workstreams/` folders for parallel chat-session work. Each workstream
creates structured handoff artifacts. The Orchestrator reads the handoffs,
checks them against contracts, resolves conflicts, and only then updates root
project memory or `game_project/`.

## Architecture

```text
Project_game/
├─ AGENTS.md
├─ CONTEXT.md
├─ orchestrator_project/
├─ docs/
│  ├─ contracts/
│  ├─ prd/
│  ├─ adr/
│  ├─ issues/
│  ├─ reports/
│  └─ blueprints/
├─ workstreams/
│  ├─ character_design/
│  ├─ illustration/
│  ├─ storyline/
│  ├─ physics_engine/
│  ├─ npc_system/
│  ├─ ui_hud/
│  ├─ level_design/
│  ├─ progression_system/
│  └─ daily_activities/
│     ├─ shared/
│     ├─ fishing/
│     ├─ farming/
│     ├─ factory_work/
│     ├─ cooking/
│     ├─ foraging/
│     ├─ crafting/
│     └─ template_activity/
├─ game_project/
├─ data/
└─ runs/
```

## Roles

- `orchestrator_project/`: reusable AI operating framework.
- `docs/contracts/`: central agreements every workstream must obey.
- `workstreams/`: isolated chat-session workspaces.
- `CONTEXT.md`: accepted game memory after Orchestrator review.
- `game_project/`: final implementation target after review.

## Workstream Rule

A workstream does not directly update `CONTEXT.md`, `docs/contracts/`, or
`game_project/` unless explicitly authorized. It proposes changes through:

- `HANDOFF.md`
- `proposed_context_updates.md`
- `proposed_adr.md`
- focused artifacts under `artifacts/`
- verification notes under `tests/`

## Orchestrator Merge Flow

1. Read root `AGENTS.md` and `CONTEXT.md`.
2. Read all relevant `docs/contracts/*` files.
3. Read only each selected workstream's `HANDOFF.md` first.
4. Read `proposed_context_updates.md` and `proposed_adr.md`.
5. Open `OUTPUT.md` or `artifacts/` only when a conflict or missing detail
   requires it.
6. Build a conflict table.
7. Accept, revise, or reject each proposed change.
8. Update root `CONTEXT.md`, `docs/contracts/`, `docs/adr/`, and `docs/issues/`
   only after review.
9. Apply approved implementation changes to `game_project/`.
10. Write an integration report under `docs/reports/`.

## Daily Activities and Proficiency

Daily activities are extensible. Each activity defines its own loop, tools,
places, risks, rewards, XP events, and unlock candidates. The central
`progression_system/` owns the proficiency model, XP curves, level effects,
storage shape, and UI contract.

Responsibility split:

- `daily_activities/*`: activity-specific XP events and unlock proposals.
- `progression_system/`: central proficiency rules and balance model.
- `level_design/`: spatial placement, pacing, regional difficulty, and activity
  access over time.

`level_design/` does not own proficiency formulas. It consumes progression rules
to place activity opportunities and skill-gated regions.

## Context Window Strategy

Each chat session reads only:

- root `AGENTS.md`
- relevant root `CONTEXT.md` sections
- `docs/contracts/game_vision.md`
- domain-specific contract files
- its own workstream `BRIEF.md`

The Orchestrator reads handoffs first and only descends into detailed outputs
when necessary.
