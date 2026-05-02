# Project Architect Implementation Report

## Scope

Added Project Architect as a role separate from the Orchestrator and game
development workstreams.

## Added

- `orchestrator_project/skills/project-architect/SKILL.md`
- `orchestrator_project/workflows/project_architect.md`
- `docs/guides/project_architect_workflow.md`

## Updated

- `orchestrator.config.json` now includes the `project_architect` route.
- `orchestrator_project/context_manager/select_skill.py` selects
  `project-architect`.
- `scripts/check_router_sync.py` verifies the new route.
- `scripts/run_quality_gate.ps1` dry-runs the Project Architect route.
- `workspace_policy.json` includes a Project Architect role and workspace guard
  modes.
- User-facing docs reference the Project Architect workflow.

## Role Boundary

Project Architect owns workspace structure, workflow clarity, guardrails,
routes, skills, and workstream scaffolding.

The Orchestrator still owns game direction, workstream acceptance, central game
memory promotion, and `game_project/` integration.

## Orchestrator Memory Policy

Default:

- Project Architect writes reports and `docs/orchestrator/pending_memory_update.md`.
- Orchestrator applies final `ORCHESTRATOR_MEMORY.md` changes.

Exception:

- With explicit user approval, Project Architect may update
  `ORCHESTRATOR_MEMORY.md` only for structural facts.

## Validation

Validated by router sync and quality gate after implementation.
