# Workspace Continuity Workflow

Use this workflow when the user is ending a session, starting a new chat,
renaming or moving the folder, switching machines, or recovering from stale chat
context.

## Goal

Make the workspace recoverable from files instead of conversation history.

## Flow

1. Identify the continuity mode:
   - Orchestrator close
   - Workstream close
   - Orchestrator resume
   - Workstream resume
   - Folder rename or move
   - Machine switch
2. Confirm the project root and Git state.
3. Read the minimum recovery files for the selected mode.
4. Check whether durable state files are stale or incomplete.
5. Update only the files allowed for the current role.
6. Run the quality gate when practical.
7. Report the exact next prompt a future chat should use.

## Role Boundaries

### Orchestrator

The Orchestrator may propose or apply updates to:

- `CONTEXT.md`
- `docs/contracts/*`
- `docs/prd/*`
- `docs/adr/*`
- `docs/reports/*`
- `docs/orchestrator/ORCHESTRATOR_MEMORY.md`
- `game_project/*`

Central updates still require user confirmation when they change accepted
project direction.

### Workstream

A workstream may update only its own workstream folder unless explicitly
authorized by the Orchestrator.

Required closeout files:

- `OUTPUT.md`
- `HANDOFF.md`
- `proposed_context_updates.md`
- `proposed_adr.md`

## Output

Return:

1. Selected mode
2. Files read
3. State recovered or preserved
4. Files changed or needing changes
5. Git and quality-gate status
6. Risks
7. Next prompt for the future chat
