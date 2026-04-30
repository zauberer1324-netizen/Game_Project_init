# Progression Contract

## Purpose

Define the central proficiency system used by daily activities, NPC interactions,
crafting, and long-term player growth.

## Design Direction

The proficiency system should feel grounded, practical, and action-driven:
repeated meaningful actions grant experience, higher proficiency improves
reliability and efficiency, and early levels should visibly reduce friction.

## Central Ownership

`workstreams/progression_system/` owns:

- Skill list
- XP curve
- Level range
- XP event validation rules
- Skill effect categories
- Level unlock rules
- Multipliers and learning modifiers
- Save data shape
- UI display contract
- Balance review of all activity XP proposals

## Activity Ownership

Each daily activity owns:

- Which events produce XP
- Suggested XP event weight
- Activity-specific failure reductions
- Activity-specific unlock proposals
- Activity-specific feedback and test cases

## Skill Model Draft

A skill should eventually define:

- `skill_id`
- Display name
- Category
- Maximum level
- XP curve reference
- XP event sources
- Level effects
- Unlocks
- UI presentation

## Balance Rules

- Avoid rewarding trivial repeated clicks without meaningful time, risk, or
  resource cost.
- Avoid letting one activity level unrelated skills unless explicitly designed.
- Make early levels reduce friction.
- Make later levels unlock efficiency, quality, insight, or advanced actions.
- Keep skill effects explainable to the player.
