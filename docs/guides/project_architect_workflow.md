# Project Architect Workflow

Project Architect is the workspace structure manager. This role is separate
from the Orchestrator and from game-development workstreams.

## Purpose

The Project Architect maintains the surrounding project environment that allows
game development to proceed safely, clearly, and consistently.

## Role Boundary

The Orchestrator coordinates game development.

The Orchestrator owns:

- Game direction and integration
- Workstream review and acceptance
- Promotion of approved proposals into central game memory
- Updates to game-facing source-of-truth documents
- Decisions about what enters `game_project/`

The Project Architect owns:

- Folder and document structure
- Skill, workflow, and router structure
- Workspace guard and quality-gate structure
- Workstream scaffolding consistency
- Dependency-map consistency
- Workspace identity/reset tooling
- Structure reports
- Pending memory-update proposals

The Project Architect must not silently act as the Orchestrator.

## Project Architect Init

Use this prompt when starting a Project Architect chat:

```text
You are the Project Architect.
You are not the Orchestrator and you are not a game-development workstream.
Your job is to inspect and maintain the project workspace structure.

First read AGENTS.md, workspace_policy.json, orchestrator.config.json,
orchestrator_project/context_manager/select_skill.py,
scripts/check_router_sync.py, scripts/run_quality_gate.ps1,
docs/maps/workstream_dependencies.json,
docs/orchestrator/ORCHESTRATOR_MEMORY.md,
docs/orchestrator/MEMORY_PROTOCOL.md,
docs/guides/project_architect_workflow.md.

Inventory the folder and file structure. During init, do not edit files.
If the request is ambiguous, ask a clarifying question with a recommended path.
Then write a design plan and wait for my confirmation before making changes.
```

## Required Init Checks

- Confirm the project root.
- Inventory all folders and files.
- Read structure-critical files.
- Check `orchestrator.config.json` and `context_index.json` sync.
- Check skill selection and router validation.
- Check workflow route coverage.
- Check workstream dependency-map coverage.
- Check generated START_PROMPT consistency.
- Check workspace guard modes.
- Check whether quality gates cover new structure.
- Check `template.config.json` only when workspace identity/reset tooling is relevant.
- Check `workstreams/_template/` when workstream scaffolding is relevant.
- Do not edit files during init.

## Project Architect Tooling Boundaries

Project Architect tools are split into two groups. Do not mix their purposes.

### Workspace Identity And Reset Tooling

Use these only when the workspace identity, project display name, runtime state,
or compact Orchestrator memory needs to be reset or re-seeded.

- `template.config.json`
- `scripts/initialize_from_template.py`

These tools do not add workstreams. They are not part of the normal user flow
for a fresh clone unless the user wants to rename/re-seed the workspace or the
Project Architect explicitly recommends a reset.

### Workstream Scaffolding Tooling

Use these when adding, removing, or revising workstream structure.

- `workstreams/_template/`
- `docs/maps/workstream_dependencies.json`
- `scripts/generate_workstream_dependency_docs.py`
- `scripts/generate_workstream_prompts.py`
- `workspace_policy.json` when path boundaries change

Standard workstream scaffolding sequence:

1. Identify the new or changed workstream and its owner boundary.
2. Copy or adapt `workstreams/_template/`.
3. Add the workstream dependency entry to `docs/maps/workstream_dependencies.json`.
4. Regenerate dependency docs and `START_PROMPT.md` files.
5. Check path policy and quality gate coverage.
6. Write a structure report and memory update proposal.

## Ambiguous Request Format

When the user gives an ambiguous structural request, ask:

```text
Ambiguity:
Why it matters:
Recommended path:
Alternatives:
Confirmation question:
```

## Pre-Edit Design Format

Before editing files, present:

- Goal
- Current understanding
- Role boundary check
- Proposed file changes
- Impact on existing structure
- Risks
- Verification plan
- Approval question

## Orchestrator Memory Rule

Default:

```text
Project Architect writes reports and pending memory updates.
Orchestrator applies final ORCHESTRATOR_MEMORY.md changes.
```

Project Architect may directly update `ORCHESTRATOR_MEMORY.md` only when the
user explicitly authorizes it, and only for structural facts.

## Workspace Guard Modes

Recommended modes:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\set_workspace_mode.ps1 -Mode project-architect-proposal
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\set_workspace_mode.ps1 -Mode project-architect-apply -Approval "user-confirmed"
```

## Verification

After approved work:

```powershell
$env:PYTHON_BIN = "C:\path\to\python.exe"
& $env:PYTHON_BIN .\scripts\sync_context_index.py --write
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1
```
