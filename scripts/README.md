# Scripts

Project-level helper scripts are grouped by role. Most Python scripts use only
the Python standard library. Use Python 3.10+ when practical.

## Project Architect Tools

| Script | Purpose |
| --- | --- |
| `initialize_from_template.py` | Workspace identity/reset tool for project-name replacement, runtime cleanup, and compact memory reset. Not for adding workstreams. |
| `generate_workstream_dependency_docs.py` | Regenerates dependency map and Mermaid graph from `docs/maps/workstream_dependencies.json`. |
| `generate_workstream_prompts.py` | Regenerates workstream `START_PROMPT.md` files from dependency mappings and BRIEFs. |
| `scaffold_engine_profile.py` | Copies the selected engine profile and Game Test Gate into `game_project/` after engine selection. |
| `sync_context_index.py` | Syncs `orchestrator.config.json` context routes into `orchestrator_project/context_manager/context_index.json`. |

## Quality Gate And Guardrails

| Script | Purpose |
| --- | --- |
| `run_quality_gate.ps1` | Runs the standard local verification suite. |
| `check_path_policy.py` | Checks staged or explicit files against workspace path policy. |
| `check_workspace_mode.py` | Checks optional workspace guard mode state. |
| `check_router_sync.py` | Verifies route, workflow, and skill sync. |
| `check_schema_examples.py` | Verifies schema example coverage. |
| `check_memory_freshness.py` | Warns when central memory may lag newer reports, PRDs, ADRs, or handoffs. |
| `check_workstream_dependencies.py` | Verifies workstream dependency mappings and prompt contract lists. |
| `check_start_prompts.py` | Verifies each workstream has a usable `START_PROMPT.md`. |
| `check_engine_profiles.py` | Verifies engine profile document structure. |
| `check_init_completion.py` | Optional strict check for whether `orchestrator-init` has recorded a north star, engine status, workstream status, and first PRD. Not part of the default quality gate. |

## Orchestrator And Review Helpers

| Script | Purpose |
| --- | --- |
| `run_project_orchestrator.py` | Builds a project-aware Orchestrator prompt or dry-run. |
| `draft_memory_update.py` | Drafts a pending memory update from current project state. |
| `build_merge_preview.py` | Builds a workstream merge preview for Orchestrator review. |
| `verify_merge_ready.py` | Checks whether a workstream has the minimum handoff files for review. |

## Git Hook Setup

| Script | Purpose |
| --- | --- |
| `install_git_hooks.ps1` | Sets `core.hooksPath` to `.githooks`. |
| `set_workspace_mode.ps1` | Enables optional soft workspace mode guard. |
| `clear_workspace_mode.ps1` | Clears optional workspace mode guard state. |

## Notes

This workspace is Windows/PowerShell-first. Some Python helpers are portable,
but the standard quality-gate entrypoint is `run_quality_gate.ps1`.
