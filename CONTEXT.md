# Project Game

This context is the living memory for the game project. It should contain
game-specific terms, mechanics, rules, relationships, decisions, and ambiguity
notes. Reusable AI workflow rules belong in `orchestrator_project/`, not here.

## Language

**Game Project**:
The actual playable game and its source code, assets, tests, and build setup.
_Avoid_: orchestrator project.

**Operating Framework**:
The reusable AI workflow, skill, schema, and validation scaffold stored in
`orchestrator_project/`.
_Avoid_: game codebase.

**Game Memory**:
The project-specific context, PRDs, ADRs, implementation issues, run logs, and
reports stored at the `Project_game` root.
_Avoid_: framework docs.

**Vertical Slice**:
A small piece of game work that produces a playable or verifiable increment
across the needed layers.
_Avoid_: layer task, isolated subsystem task.

**Mechanic**:
A player-facing rule or interaction that affects gameplay.
_Avoid_: implementation detail.

**Verification Checklist**:
A concrete list of scenarios that must pass before a mechanic or fix is
considered done.
_Avoid_: vibes, looks okay.

## Relationships

- The **Operating Framework** guides how AI works.
- The **Game Memory** records what this specific game is becoming.
- A **Vertical Slice** implements one narrow, verifiable part of the **Game
  Project**.
- A **Mechanic** should have a **Verification Checklist** when implemented or
  changed.

## Accuracy Rules

1. Separate game design decisions from implementation details.
2. Record durable game-specific decisions in `docs/adr/`.
3. Record feature requirements in `docs/prd/`.
4. Record implementation slices in `docs/issues/`.
5. Record bug reproduction and verification notes in `runs/` or
   `docs/reports/`.
6. If external factual claims are used, store evidence under `data/`.

## Game Development Rules

1. Build playable vertical slices.
2. Prefer deterministic mechanics tests where practical.
3. For physics or movement bugs, reproduce before fixing.
4. Track inputs, position, velocity, collision state, and timers for movement
   diagnostics.
5. Distinguish prototype shortcuts from durable architecture decisions.

## Example Dialogue

> **User:** "Make a 2D platformer with dash and wall jump."
> **AI:** "I will use `orchestrator_project` as the workflow framework, record
> game-specific terminology in root `CONTEXT.md`, create a PRD under
> `docs/prd/`, split implementation into vertical slices under `docs/issues/`,
> and put actual code in `game_project/`."

## Flagged Ambiguities

- No concrete game genre, engine, target platform, or art direction has been
  chosen yet.
- `game_project/` is currently a placeholder until an engine or stack is
  selected.


## Workstream Language

**Workstream**:
A scoped workspace for one chat session or specialist task that produces reviewable handoff artifacts.
_Avoid_: final branch, source of truth.

**Contract**:
A central agreement under `docs/contracts/` that workstreams must obey until the Orchestrator accepts a change.
_Avoid_: suggestion, note.

**Handoff**:
A compact workstream summary that the Orchestrator reads before detailed outputs.
_Avoid_: full transcript, raw notes.

**Daily Activity**:
An expandable everyday gameplay loop such as fishing, farming, factory work, cooking, foraging, or crafting.
_Avoid_: minigame unless the activity is intentionally isolated.

**Proficiency System**:
The central progression model that turns meaningful repeated actions into skill growth, reliability, efficiency, insight, and unlocks.
_Avoid_: per-activity level formula.

**Level Design**:
The design of regions, routes, resources, activity access, risk placement, pacing, and spatial progression.
_Avoid_: proficiency system.

## Workstream Relationships

- A **Workstream** produces a **Handoff**.
- A **Contract** constrains all related **Workstreams**.
- A **Daily Activity** proposes XP events and unlock candidates.
- The **Proficiency System** owns XP curves, level effects, and global balance.
- **Level Design** places activities and proficiency requirements into the world.
- The Orchestrator is the only actor that promotes proposals into root `CONTEXT.md`, `docs/contracts/`, `docs/adr/`, `docs/issues/`, or `game_project/`.
