# Project Game Workspace

This workspace separates the reusable AI operating framework from the actual
game project memory and code.

## Structure

```text
Project_game/
|- AGENTS.md                  # Root rules for AI work in this workspace
|- CONTEXT.md                 # Game-specific living memory
|- docs/                      # Game-specific PRDs, ADRs, issues, reports
|- data/                      # Game-specific evidence artifacts
|- runs/                      # Game-specific run logs and generated prompts
|- scripts/                   # Project-level helpers
|- orchestrator_project/      # Reusable AI operating framework
`- game_project/              # Actual game code and assets
```

## How To Use

For substantial game work, ask the AI to use `orchestrator_project` as the
operating framework while writing project-specific memory to the root workspace.

Example:

```text
Use this workspace's AGENTS.md rules.
Use orchestrator_project as the operating framework.
Create a 2D platformer plan, record game-specific context in root CONTEXT.md,
write the PRD under docs/prd, split implementation into docs/issues, and put
actual code under game_project.
```

## Dry Run

Generate a prompt using root project memory and framework skills:

```powershell
python .\scripts\run_project_orchestrator.py --request "Make a 2D platformer prototype" --intent game_dev --task-type feature --risk medium --dry-run
```

## Full User Guide

Read the detailed Korean guide here:

- `docs/USER_GUIDE.md`

## Parallel Workstreams

Separate chat sessions should work under `workstreams/` and produce handoff
artifacts instead of directly changing central project memory.

Read the detailed blueprint:

- `docs/blueprints/multi-workstream-orchestration.md`

Key rule:

```text
workstreams propose, Orchestrator integrates.
```

## Audio Workstreams

Audio production is split into `workstreams/bgm/` and
`workstreams/game_sound/`. Both are proposal spaces. Accepted audio decisions
should be reviewed by the Orchestrator and promoted into `docs/contracts/`,
`docs/adr/`, `docs/prd/`, `docs/issues/`, or `game_project/` only after review.

The central audio rules live in:

- `docs/contracts/audio_contract.md`

## Guardrails

Install git hooks after creating or copying a project workspace:

```powershell
git init
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\install_git_hooks.ps1
```

Run the quality gate:

```powershell
$env:PYTHON_BIN = "C:\path\to\python.exe"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1
```

The guardrails check path policy, router sync, schema examples, memory freshness,
workstream dependencies, start prompts, engine profiles, workspace mode, and
orchestration dry-runs.

## New Game Startup

Start with:

- `docs/startup/GAME_SEED_TEMPLATE.md`
- `docs/startup/NEW_GAME_START_CHECKLIST.md`
- `docs/startup/INIT_COMPLETION_CRITERIA.md`

Open specialist workstream chats with the matching `START_PROMPT.md` file under
that workstream folder.

## Engine Profiles

Engine-specific build and test gates live under `engine_profiles/`. After an
engine is selected, copy its Game Test Gate into `game_project/test_config/`:

```powershell
python .\scripts\scaffold_engine_profile.py phaser_typescript --write
```

Use the selected profile's Game Test Gate as the project-specific game test
layer in addition to the workspace quality gate.

## Workspace Continuity

Before renaming or moving the folder, switching machines, or starting a new chat,
use the `workspace-continuity` skill and read:

- `docs/guides/workspace_continuity.md`
- `docs/orchestrator/ORCHESTRATOR_MEMORY.md`

The goal is to recover state from files instead of relying on previous chat
context.

## Workspace Guard

Optional soft locks for workstream and Orchestrator modes are documented in:

- `docs/guides/workspace_guard.md`

## Environment

This workspace is Windows/PowerShell-first. Python helpers use the standard
library unless a game-specific engine profile adds its own dependencies. Use
Python 3.10+ when practical.

## Project Architect

Use `project-architect` for workspace structure management, not game direction.
Read:

- `docs/guides/project_architect_workflow.md`
- `orchestrator_project/skills/project-architect/SKILL.md`

Project Architect also owns workspace identity/reset tooling such as
`template.config.json` and `scripts/initialize_from_template.py`. These are not
normal Orchestrator tools and are not used to add workstreams.
