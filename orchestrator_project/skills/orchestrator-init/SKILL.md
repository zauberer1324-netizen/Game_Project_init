---
name: orchestrator-init
description: Initializes a game project before parallel workstreams begin. Uses a grill-with-docs style interview to align game vision, context, contracts, first PRD, engine choice or deferral, workstream briefs, and Orchestrator memory. Use when starting a new game project, resetting direction, or before opening specialist workstream chats.
---

# Orchestrator Init

## Role

Act as the Main Orchestrator setting the project's north star before any
specialist workstreams begin.

This skill is not for implementation. It is for alignment, memory setup, engine
choice or deferral, and workstream readiness.

## Goal

Create enough shared direction that all workstreams can produce compatible
outputs.

## Source Of Truth Rules

- `CONTEXT.md` holds accepted game language and rules.
- `docs/contracts/*` holds shared constraints all workstreams must obey.
- `docs/prd/*` holds scoped product requirements.
- `docs/adr/*` records durable decisions such as engine selection.
- `docs/orchestrator/ORCHESTRATOR_MEMORY.md` is an operational index and status
  board for the Orchestrator. It is not the source of truth.
- Workstream folders should not start serious work until the initial memory,
  contracts, PRD, engine status, and BRIEFs are ready.

## Process

### 1. Read Existing Memory

Read, if present:

1. `AGENTS.md`
2. `CONTEXT.md`
3. `docs/orchestrator/ORCHESTRATOR_MEMORY.md`
4. `docs/contracts/game_vision.md`
5. `docs/contracts/gameplay_contract.md`
6. `docs/contracts/progression_contract.md`
7. `docs/contracts/daily_activity_contract.md`
8. `docs/contracts/code_interface_contract.md`
9. `engine_profiles/README.md`
10. existing `docs/prd/*`
11. existing `workstreams/*/BRIEF.md`

Do not treat blank template text as accepted decisions.

### 2. Grill The User

Ask one question at a time. For each question:

- Explain why it matters.
- Provide your recommended answer.
- Wait for the user's response.
- Track whether the answer is accepted, assumed, or still open.

Required topics:

- One-sentence game pitch
- Core player fantasy
- Primary loop
- Secondary loops
- Genre
- Camera or perspective
- Target platform
- Target runtime or platform constraints
- Session length
- First playable prototype scope
- Explicit out-of-scope items
- Visual tone
- Narrative tone
- Daily activity importance
- Proficiency system philosophy
- First 10 minutes of play
- Engine selection, or explicit deferral with reason
- Engine profile to attach from `engine_profiles/`, if selected
- Workstreams needed for the first milestone

### 3. Produce Draft Plan

After enough answers, propose updates for:

- `CONTEXT.md`
- `docs/contracts/game_vision.md`
- `docs/contracts/gameplay_contract.md`
- `docs/contracts/progression_contract.md`
- `docs/contracts/daily_activity_contract.md` if daily activities matter early
- `docs/contracts/code_interface_contract.md` if an engine is selected or enough
  runtime constraints are accepted
- `docs/prd/prototype-1.md`
- `docs/adr/000X-engine-selection.md` if the engine is selected or explicitly
  deferred
- selected `workstreams/*/BRIEF.md`
- `docs/orchestrator/ORCHESTRATOR_MEMORY.md`

If an engine is selected, propose attaching the selected profile with
`scripts/scaffold_engine_profile.py` after user confirmation. Do not run the
scaffold step silently during planning.

Separate:

- Accepted decisions
- Assumptions
- Open questions
- Later decisions
- Engine status: selected or deferred with reason
- Workstream blockers caused by engine deferral

### 4. Show Before Editing

Before editing files, show the planned changes grouped by file. Ask for user
confirmation.

Do not silently convert assumptions into accepted decisions.

### 5. Update Orchestrator Memory

When confirmed, create or update `docs/orchestrator/ORCHESTRATOR_MEMORY.md` with:

- Current project phase
- Current north star summary
- Selected engine, or `deferred` with reason and affected workstreams
- Accepted decision index with links to source files
- Open questions
- Workstreams ready to start
- Workstreams blocked
- Last orchestration action
- Next recommended orchestration action

This memory file should point to `CONTEXT.md`, contracts, PRDs, ADRs, and
reports. It should not duplicate long source content.

### 6. Completion Criteria

Done when:

- Root project memory has enough direction for workstreams.
- The first PRD exists or is drafted.
- Relevant contracts contain usable direction.
- Engine selection is recorded, or deferral is explicit with reason.
- Engine-dependent workstreams are ready or clearly blocked.
- Workstream briefs are ready or clearly blocked.
- Orchestrator memory has a compact status summary.
- Open questions are listed.
