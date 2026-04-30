# Single Source Cleanup Report

## Purpose

Remove the last duplicated maintenance points before committing the reusable game
orchestration workspace.

## Changes

- Added `docs/maps/workstream_dependencies.json` as the single source for
  workstream-to-contract dependencies.
- Reworked `scripts/generate_workstream_prompts.py` to read dependency data from
  `workstream_dependencies.json` instead of hardcoded `_contract_list_for()`
  logic.
- Added `scripts/workstream_dependency_lib.py` for shared dependency loading and
  workstream discovery.
- Added `scripts/check_workstream_dependencies.py` to verify dependency coverage,
  contract file existence, and START_PROMPT consistency.
- Added `scripts/generate_workstream_dependency_docs.py` so
  `workstream_dependency_map.md` and `workstream_dependency_graph.mmd` are
  generated from the JSON source.
- Added `scripts/sync_context_index.py` so `orchestrator.config.json` remains the
  source of truth and `orchestrator_project/context_manager/context_index.json`
  is a checked mirror.
- Updated `scripts/check_router_sync.py` to fail when context routes differ
  between config and mirror.
- Updated `orchestrator_project/context_manager/select_context.py` to use the
  project config when available, with framework-local index fallback.
- Regenerated workstream dependency docs and START_PROMPT files.

## Verification

Quality gate passed:

```text
context index sync check passed
router sync check passed
schema example check passed
memory freshness check passed
path policy check passed
workstream dependency check passed
start prompt check passed
engine profile check passed
path policy check passed
quality gate passed
```

## Remaining Note

`Project_Game_init/` was created externally as a separate local repository and is
not part of this workspace template commit.