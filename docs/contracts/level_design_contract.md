# Level Design Contract

## Purpose

Define how regions, maps, encounters, activity access, resources, and pacing are
planned.

## Responsibility

`workstreams/level_design/` owns:

- Region structure
- Player route and pacing
- Resource density
- Activity placement
- Risk placement
- Tutorial flow
- Skill-gated location proposals
- Reward distribution

It does not own proficiency formulas or XP curves. It consumes
`progression_contract.md` and activity handoffs to place opportunities in the
world.

## Required Fields To Resolve

- Region list
- Entry conditions
- Activity availability by region
- Expected proficiency range by region
- Resource and reward distribution
- Risk and recovery placement
- Navigation constraints
- Verification checklist
