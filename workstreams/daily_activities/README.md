# Daily Activities Workstream Group

Daily activities are expandable gameplay loops that represent everyday work,
survival, production, gathering, care, or craft actions.

Each activity owns its own action loop, tools, locations, risks, rewards, XP
events, and unlock proposals. The central proficiency rules are owned by
`workstreams/progression_system/`.

## Add A New Activity

1. Copy `template_activity/`.
2. Rename the folder to a clear activity id.
3. Fill `activity_spec.md`, `skill_events.md`, and `unlocks.md`.
4. Write a compact `HANDOFF.md` for Orchestrator review.
5. Do not edit root `CONTEXT.md`, contracts, or `game_project/` directly.
