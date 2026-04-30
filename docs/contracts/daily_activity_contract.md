# Daily Activity Contract

## Purpose

Define the common schema for expandable daily activities such as fishing,
farming, factory work, cooking, foraging, crafting, and future activities.

## Activity Schema

Each activity must define:

- `activity_id`
- Player fantasy
- Core action loop
- Required tools
- Required location types
- Required inputs
- Time cost
- Resource cost
- Risk or failure conditions
- Output rewards
- XP events
- Proficiency effects
- Unlock candidates
- UI feedback
- Animation and audio needs
- Verification checklist

## Extension Rule

New daily activities should be created by copying
`workstreams/daily_activities/template_activity/` and filling the activity
schema. Shared behavior belongs in `workstreams/daily_activities/shared/`.

## Ownership

Daily activity workstreams own activity-specific proposals. They do not own the
central proficiency curve, level formula, save data shape, or global UI contract.
Those belong to `workstreams/progression_system/`.
