# Project Architect Workflow

Use this workflow when the user asks to inspect, design, or modify the project
workspace structure rather than the game itself.

## Goal

Keep the workspace structure coherent without taking over Orchestrator authority
or game-development decisions.

## Flow

1. Identify whether the request is:
   - Project Architect init
   - Structure review
   - Workstream scaffold design
   - Skill/workflow/router update
   - Guardrail or quality-gate update
   - Template maintenance
2. Confirm role boundaries.
3. Inventory the full folder/file structure.
4. Read structure-critical files.
5. Identify ambiguities and ask with recommendations when needed.
6. Produce a design plan before edits.
7. Wait for user approval.
8. Apply approved structural changes only.
9. Generate or update reports and pending memory updates.
10. Run sync and quality checks.

## Source Of Truth

- Project structure rules live in `AGENTS.md`, `workspace_policy.json`,
  `orchestrator.config.json`, `orchestrator_project/context_manager/`,
  `scripts/`, and `docs/guides/`.
- Workstream dependencies live in `docs/maps/workstream_dependencies.json`.
- Generated dependency docs and START_PROMPT files must match their source data.
- Game memory remains owned by the Orchestrator and game-facing documents.

## Output

Return:

1. Task interpretation
2. Role boundary check
3. Files and folders inspected
4. Ambiguities and recommendations
5. Proposed design
6. Files expected to change
7. Verification plan
8. Approval request or completed result
