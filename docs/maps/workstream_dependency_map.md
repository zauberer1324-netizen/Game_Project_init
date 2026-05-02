# Workstream Dependency Map

This map is generated from `docs/maps/workstream_dependencies.json`.
Edit that JSON file first, then regenerate this document.

## Source Of Truth

- `CONTEXT.md` holds accepted game memory.
- `docs/contracts/*` holds shared constraints.
- `docs/maps/workstream_dependencies.json` is the single source for workstream
  contract dependencies.
- Workstream files are proposals until the Orchestrator accepts them.

## Contract Dependencies

| Workstream | Required Contracts | Why |
| --- | --- | --- |
| `character_design/` | `game_vision.md`, `art_direction.md`, `narrative_contract.md` | Character designs must match the game fantasy, visual tone, and world logic. |
| `illustration/` | `game_vision.md`, `art_direction.md`, `asset_pipeline_contract.md` | Illustration output must fit the visual direction and asset pipeline. |
| `storyline/` | `game_vision.md`, `narrative_contract.md` | Story output defines or depends on setting, tone, conflict, and character voice. |
| `physics_engine/` | `gameplay_contract.md`, `code_interface_contract.md` | Physics behavior must match player-facing rules and implementation interfaces. |
| `npc_system/` | `narrative_contract.md`, `gameplay_contract.md`, `code_interface_contract.md` | NPCs connect world logic, gameplay behavior, and code interfaces. |
| `ui_hud/` | `gameplay_contract.md`, `progression_contract.md`, `art_direction.md`, `code_interface_contract.md` | UI must present gameplay state, proficiency, and visual tone consistently. |
| `level_design/` | `game_vision.md`, `gameplay_contract.md`, `daily_activity_contract.md`, `progression_contract.md`, `level_design_contract.md` | Level design owns spatial pacing, activity placement, and skill-gated locations. |
| `progression_system/` | `game_vision.md`, `gameplay_contract.md`, `daily_activity_contract.md`, `progression_contract.md`, `code_interface_contract.md` | Progression owns central proficiency rules, XP curves, unlocks, UI contract, and save shape. |
| `daily_activities/*` | `game_vision.md`, `daily_activity_contract.md`, `progression_contract.md` | Activities propose loops, risks, rewards, XP events, and unlock candidates. |
| `bgm/` | `game_vision.md`, `narrative_contract.md`, `audio_contract.md`, `asset_pipeline_contract.md` | BGM must match the game fantasy, narrative tone, audio standards, and asset provenance rules. |
| `game_sound/` | `game_vision.md`, `gameplay_contract.md`, `audio_contract.md`, `asset_pipeline_contract.md`, `code_interface_contract.md` | Game sound must match player-facing gameplay, shared audio standards, asset rules, and implementation event interfaces. |

## Ownership Boundaries

- `daily_activities/*` owns activity-specific loops, risks, rewards, XP event
  proposals, unlock candidates, and verification notes.
- `progression_system/` owns central skill definitions, XP curves, level
  effects, save data shape, UI display contract, and balance review.
- `level_design/` owns regions, routes, activity placement, resource density,
  risk placement, pacing, and skill-gated location proposals.
- `level_design/` must not own XP formulas or central proficiency curves.
- `bgm/` owns background music direction proposals, cue sheets, motifs, loops,
  transitions, stingers, references, and BGM asset briefs.
- `game_sound/` owns gameplay SFX proposals, UI audio proposals, ambience
  proposals, audio event naming proposals, playback priority, variation, and
  verification notes.
- Audio workstreams may propose sound needs, but the Orchestrator promotes only
  accepted audio decisions into contracts, ADRs, PRDs, issues, or implementation.
- Workstreams must not directly promote proposals into `CONTEXT.md`,
  `docs/contracts/`, `docs/adr/`, `docs/issues/`, or `game_project/`.

## Startup Order Recommendation

1. Run `orchestrator-init`.
2. Fill `game_vision.md`, `gameplay_contract.md`, and the first PRD.
3. Fill `art_direction.md` before serious character or illustration work.
4. Fill `narrative_contract.md` before serious storyline or NPC work.
5. Fill `progression_contract.md` before serious daily activity balancing.
6. Fill `code_interface_contract.md` before code-oriented parallel work.
7. Start only the workstreams marked ready in `docs/orchestrator/ORCHESTRATOR_MEMORY.md`.
