# Template Reuse Enhancement Report

## Purpose

Improve the workspace as a reusable new-game starting table while preserving the
project's intent: engine neutrality, creative workstream freedom, and
Orchestrator-reviewed integration.

## Implemented

- Added startup documents under `docs/startup/`.
- Added workstream `START_PROMPT.md` generation and checks.
- Generated `START_PROMPT.md` files for existing workstreams and daily activity
  folders.
- Added `template.config.json` and `scripts/initialize_from_template.py`.
- Added `scripts/draft_memory_update.py` for pending Orchestrator memory update
  drafts.
- Added merge preview template and scripts.
- Added engine profiles under `engine_profiles/`.
- Added engine-specific `Game Test Gate` sections to each profile.
- Added `scripts/scaffold_engine_profile.py` to copy the selected profile's test
  gate into `game_project/test_config/`.
- Added design, handoff, implementation, and art rubrics.
- Added git branch, commit, and PR protocol documents.

## User Clarification Applied

Engine-specific game tests are not a separate pre-engine requirement. They live
inside each engine adapter profile and become active when that profile is
selected.

## Verification

The quality gate now checks:

- router sync
- schema examples
- memory freshness
- path policy
- workstream start prompts
- engine profiles
- orchestration dry-runs
- template initialization dry-run
- memory draft dry-run
- merge preview dry-run

## Remaining Intentional Flexibility

- `game_project/` remains engine-neutral until an engine profile is selected.
- Workstream creativity remains prompt- and user-guided.
- Integration remains Orchestrator-reviewed rather than automatic.
