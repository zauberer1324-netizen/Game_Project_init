# Orchestrator Memory

This file is the Orchestrator's compact operational memory. It exists so a
future Orchestrator chat can recover the current project state from files after
context compression, a folder move, a machine switch, or a new chat session.

This file is not the source of truth. It is an index and status board.

## How To Use This Memory

At the start of an Orchestrator chat, read this file after `AGENTS.md`,
`orchestrator_project/AGENTS.md`, `orchestrator.config.json`, and `CONTEXT.md`.
Then confirm freshness against recent PRDs, ADRs, reports, contracts, and
workstream handoffs before acting.

Trust durable source files over this memory if they disagree:

- Accepted game language and rules: `CONTEXT.md`
- Shared constraints: `docs/contracts/`
- Product scope: `docs/prd/`
- Durable decisions: `docs/adr/`
- Structural implementation reports: `docs/reports/`
- Workstream proposals: `workstreams/*/HANDOFF.md`, `OUTPUT.md`,
  `proposed_context_updates.md`, and `proposed_adr.md`
- Accepted implementation: `game_project/`

Do not copy long content here. Link to source files and keep only the current
operational state, blockers, and next action.

## Current Project Phase

Reusable AI game-development workspace is structurally prepared. The workspace
has orchestration rules, workstreams, contracts, dependency maps, continuity
guides, optional workspace guards, Project Architect support, audio workstreams,
engine-profile scaffolding, and quality checks.

Game-specific initialization has not happened yet. The next game should begin
with `orchestrator-init` before specialist workstreams start serious work.

## Current North Star Summary

Not defined yet.

Required next step: run `orchestrator-init` with the user to define the game's
one-sentence pitch, core player fantasy, primary loop, first playable prototype
scope, initial contracts, workstream briefs, and engine status.

## Selected Engine

Not selected yet.

During `orchestrator-init`, select an engine profile from `engine_profiles/` or
explicitly defer engine selection with:

- reason for deferral
- affected or blocked workstreams
- next condition that will unblock the decision

Engine-dependent workstreams must remain blocked until engine status is
selected or explicitly deferred with clear limits.

## Operating Boundaries

- Orchestrator owns game direction synthesis, workstream review, promotion of
  accepted proposals into central files, and final coordination.
- Project Architect is a separate manager role for workspace structure, folder
  layout, skills, workflows, routers, guardrails, templates, and scaffolding.
- Specialist workstreams are proposal spaces unless the Orchestrator explicitly
  authorizes implementation mode.
- If a user asks this Orchestrator chat for structural workspace changes, ask
  them to use a separate Project Architect chat first.
- Project Architect memory exception rule remains governed by
  `docs/orchestrator/MEMORY_PROTOCOL.md`; do not broaden it from this memory
  file.

## Accepted Decision Index

- `docs/adr/0001-separate-operating-framework-from-game-memory.md` - separates
  reusable orchestration framework from game-specific memory.
- `docs/adr/0002-use-workstreams-for-parallel-chat-development.md` - uses scoped
  workstreams and Orchestrator review before central integration.
- `docs/reports/workstream-architecture-implementation-report.md` - establishes
  workstreams as separate proposal areas with central review.
- `docs/reports/workspace-continuity-implementation-report.md` - adds recovery
  workflow for folder renames, machine switches, and new chat sessions.
- `docs/reports/workspace-guard-implementation-report.md` - adds optional
  read-only workspace mode guards without ACL hard locks.
- `docs/reports/project-architect-implementation-report.md` - adds Project
  Architect as a workspace-structure role separate from Orchestrator and game
  development authority.
- `docs/reports/audio-workstream-architecture-report.md` - adds proposal-only
  `bgm/` and `game_sound/` workstreams plus the central `audio_contract.md`.
- `docs/reports/orchestrator-init-and-architect-tooling-report.md` - makes
  engine status explicit in `orchestrator-init` and documents Project Architect
  identity/reset versus workstream scaffolding tooling.
- `docs/reports/project-architect-policy-and-guide-sync-report.md` - syncs
  `docs/USER_GUIDE.md` and Project Architect path policy with the latest
  workspace structure.

## Open Questions

Initialization questions still unanswered:

- What is the one-sentence game pitch?
- What is the core player fantasy?
- What is the primary loop and first 10 minutes of play?
- What is the first playable prototype scope?
- Which engine should be selected, or why should engine selection be deferred?
- Which daily activities belong in the first milestone?
- What progression philosophy should guide proficiency and activity growth?
- What is the first prototype's audio priority: BGM mood, gameplay feedback,
  ambience, UI clarity, or silence-first implementation?

## Workstreams Ready To Start

None.

Reason: game-specific north star, prototype scope, engine status, initial
contracts, and workstream briefs are not initialized yet.

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
- `ui_hud/` - blocked on gameplay, progression, and engine/UI constraints.
- `level_design/` - blocked on game vision, progression, and daily activity
  priorities.
- `progression_system/` - blocked on progression philosophy.
- `daily_activities/*` - blocked on game vision, daily activity priority, and
  progression direction.

## Freshness And Verification Status

Last known verification:

- Standard quality gate passed after the latest guide and policy sync.
- `check_init_completion.py --warn-only` correctly reported expected warnings
  because no game-specific initialization exists yet.
- `git diff --check` passed; line-ending warnings, if shown, are not blocking.

Before the next major action, rerun the relevant checks:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1
python .\scripts\check_init_completion.py --warn-only
python .\scripts\check_memory_freshness.py
```

## Last Orchestration Action

Synced the user guide and Project Architect path policy with the latest
workspace structure. `docs/USER_GUIDE.md` now explains engine status, audio
workstreams, Project Architect tooling boundaries, script docs, data/runs usage,
and recommended startup prompts. `workspace_policy.json` now allows Project
Architect apply mode to edit structural user-facing guide and README files while
leaving the memory exception rule unchanged.

Report: `docs/reports/project-architect-policy-and-guide-sync-report.md`.

## Next Recommended Orchestration Action

For game-start work in this Orchestrator chat, run `orchestrator-init` with the
user. The goal is to produce:

- accepted game north star
- selected or deferred engine status
- first prototype scope
- initial contract updates
- first PRD
- ready-or-blocked workstream briefs
- updated Orchestrator memory

If the user's next request is about workspace structure, folders, skills,
workflows, routers, guardrails, templates, or workstream scaffolds, do not
handle it as game orchestration. Ask the user to open or switch to a separate
Project Architect chat and run Project Architect init there.
