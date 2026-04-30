---
name: workspace-continuity
description: Preserves and restores project state when ending a chat, renaming or moving the local folder, switching machines, or starting a new Orchestrator or workstream chat. Use when the user says they are closing a session, changing the folder name, reopening the workspace, continuing in a new chat, cloning on another computer, or recovering context.
---

# Workspace Continuity

## Role

Keep the project recoverable from files, not from chat memory.

This skill protects continuity across:

- Codex context compression
- New chat sessions
- Folder renames or moves
- GitHub Desktop local path changes
- Switching between laptop and desktop
- Re-cloning a game project from GitHub

## Core Rule

Do not rely on prior chat memory as the source of truth.

Use project files as the recovery source:

- `CONTEXT.md`
- `docs/contracts/*`
- `docs/prd/*`
- `docs/adr/*`
- `docs/orchestrator/ORCHESTRATOR_MEMORY.md`
- workstream `HANDOFF.md` files
- accepted files under `game_project/`

## Modes

Choose one mode before acting:

1. Orchestrator Session Close
2. Workstream Session Close
3. Orchestrator Session Resume
4. Workstream Session Resume
5. Folder Rename Or Move
6. Machine Switch

If the mode is unclear, infer the safest mode from the user's request and state
the assumption.

## Orchestrator Session Close

Use this before ending an Orchestrator chat, renaming the folder, switching
machines, or handing the project to a future Orchestrator.

### Read

1. `AGENTS.md`
2. `CONTEXT.md`
3. `docs/orchestrator/MEMORY_PROTOCOL.md`
4. `docs/orchestrator/ORCHESTRATOR_MEMORY.md`
5. Recent `docs/prd/*`, `docs/adr/*`, and `docs/reports/*`
6. Any workstream `HANDOFF.md` files newer than Orchestrator memory
7. `git status`

### Checks

- Is the current project root correct?
- Is the Git remote configured?
- Is the current branch expected?
- Are there uncommitted changes?
- Are central files newer than Orchestrator memory?
- Are workstream handoffs waiting for review?
- Are accepted decisions recorded in durable files?
- Is anything important only present in chat text?

### Actions

After user confirmation when editing central files:

- Update `docs/orchestrator/ORCHESTRATOR_MEMORY.md` if stale.
- Create or update `docs/reports/*` when a review or closeout needs a durable
  trace.
- Run the quality gate when practical.
- Recommend commit and push if the workspace should be recoverable elsewhere.

### Output

Report:

- Current project root
- Current branch and remote
- Session status
- Files changed or needing updates
- Unreviewed workstreams
- Quality gate result
- Commit/push recommendation
- Exact next prompt for a future Orchestrator chat

## Workstream Session Close

Use this before ending a specialist workstream chat.

### Read

1. `AGENTS.md`
2. `CONTEXT.md`
3. `docs/orchestrator/ORCHESTRATOR_MEMORY.md`
4. The workstream `START_PROMPT.md`
5. The workstream `BRIEF.md`
6. The workstream `OUTPUT.md`
7. The workstream `HANDOFF.md`
8. The workstream `proposed_context_updates.md`
9. The workstream `proposed_adr.md`
10. Required contracts listed in `START_PROMPT.md`

### Rules

- Work only inside the assigned workstream folder.
- Do not directly edit `CONTEXT.md`.
- Do not directly edit `docs/contracts/*`.
- Do not directly edit `docs/adr/*`, `docs/prd/*`, `docs/issues/*`, or
  `docs/reports/*`.
- Do not directly edit `game_project/*` unless the Orchestrator explicitly
  authorized implementation mode.

### Actions

- Update `OUTPUT.md` with the detailed work product.
- Update `HANDOFF.md` with a compact review-ready summary.
- Put central memory suggestions in `proposed_context_updates.md`.
- Put durable decision suggestions in `proposed_adr.md`.
- List assumptions, blockers, unresolved questions, and next recommended work.
- Ensure the Orchestrator can review without reading the whole chat.

### Output

Report:

- Workstream path
- Files updated
- What is ready for Orchestrator review
- What is blocked
- What must not be treated as accepted project memory yet
- Exact next prompt for a future workstream chat

## Orchestrator Session Resume

Use this at the start of a new Orchestrator chat, after a folder rename, after a
fresh clone, or when the user says the previous chat context may be stale.

### Read In Order

1. `AGENTS.md`
2. `orchestrator_project/AGENTS.md`
3. `orchestrator.config.json`
4. `CONTEXT.md`
5. `docs/orchestrator/ORCHESTRATOR_MEMORY.md`
6. `docs/orchestrator/MEMORY_PROTOCOL.md`
7. `docs/maps/workstream_dependency_map.md`
8. Recent `docs/reports/*`
9. Relevant `docs/contracts/*`
10. `git status`, branch, and remote when tools are available

### Checks

- Does the current folder contain the expected project root files?
- Does `orchestrator.config.json` project name match the intended game name?
- Is Orchestrator memory structurally valid?
- Is Orchestrator memory stale relative to PRDs, ADRs, reports, or handoffs?
- Are there ready or blocked workstreams?
- Is the next action initialization, review, planning, implementation, or
  recovery?

### Output

Start by summarizing:

- Project root
- Project name
- Current branch and remote
- Current phase
- North star summary
- Accepted decisions
- Open questions
- Workstreams ready to start
- Workstreams blocked
- Freshness risks
- Recommended next action

## Workstream Session Resume

Use this at the start of a new specialist workstream chat.

### Read In Order

1. `AGENTS.md`
2. `CONTEXT.md`
3. `docs/orchestrator/ORCHESTRATOR_MEMORY.md`
4. `workstreams/<name>/START_PROMPT.md`
5. `workstreams/<name>/BRIEF.md`
6. `workstreams/<name>/HANDOFF.md`
7. `workstreams/<name>/OUTPUT.md`
8. Contracts listed in `START_PROMPT.md`

### Checks

- Is this workstream marked ready or blocked?
- Are required contracts resolved enough to proceed?
- Are there unresolved assumptions from the previous session?
- Is there any proposal waiting for Orchestrator review?
- Is the requested work inside the workstream boundary?

### Output

Start by summarizing:

- Assigned workstream
- Files read
- Current workstream status
- Existing output summary
- Unaccepted proposals
- Blockers
- Safe next tasks for this chat

## Folder Rename Or Move

Before rename or move:

1. Run Orchestrator Session Close.
2. Run the quality gate when practical.
3. Commit and push important state.
4. Close Codex, GitHub Desktop, VS Code, and other tools using the folder.

After rename or move:

1. Open the new folder path as the workspace root.
2. In GitHub Desktop, add the new local repository path if needed.
3. Verify `git status` and `git remote -v`.
4. Run Orchestrator Session Resume.
5. If the internal project name changed, run the template initialization script
   and regenerate workstream prompts.

## Machine Switch

Before leaving a machine:

1. Run the relevant session close mode.
2. Commit and push.

On the next machine:

1. Clone once if the repo is not local yet.
2. Pull if the repo is already cloned.
3. Open the repo root in Codex.
4. Run the relevant session resume mode.

## Completion Criteria

Done when a future chat can continue from project files without needing hidden
chat context.
