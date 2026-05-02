# Audio Contract

## Purpose

Define how music, sound effects, UI audio, ambience, and future voice work are
planned, reviewed, promoted, and verified.

Audio decisions become accepted project rules only after Orchestrator review.
Audio workstreams are proposal spaces until their outputs are promoted into
contracts, ADRs, PRDs, issues, or implementation tasks.

## Audio Categories

- `bgm`: background music, motifs, loops, transitions, stingers, and state-based
  music direction.
- `game_sound`: gameplay sound effects, UI sound, environmental ambience, and
  interaction feedback.
- `voice`: optional future category for voice barks, dialogue recording,
  narration, and localization-sensitive speech.

## Ownership Boundaries

`workstreams/bgm/` owns music direction proposals, cue sheets, motif notes, loop
requirements, transition requirements, stinger requirements, reference notes,
and BGM asset briefs.

`workstreams/game_sound/` owns gameplay SFX proposals, UI sound proposals,
ambience proposals, audio event naming proposals, playback priority proposals,
variation notes, and verification notes.

`workstreams/storyline/` may propose scene mood, emotional pacing, chapter tone,
and music or sound needs. It does not own final BGM or SFX production.

`workstreams/ui_hud/` may propose UI feedback needs. Final UI audio production
belongs to `game_sound`.

`workstreams/level_design/` may propose regional ambience needs, spatial audio
density, and audio cues tied to navigation or risk. Final ambience production
belongs to `game_sound`.

`workstreams/npc_system/` may propose NPC reaction audio needs, state-change
audio needs, and crowd or settlement sound needs. Final sound design belongs to
`game_sound`.

## Asset Naming

Use stable, descriptive names that preserve category, context, variant, and
version.

Recommended pattern:

```text
{category}_{context}_{descriptor}_{variant}_v{number}
```

Examples:

```text
bgm_forest_explore_main_a_v01
sfx_player_pickup_wood_a_v01
ui_inventory_open_soft_a_v01
amb_town_morning_loop_a_v01
```

Asset manifests must record source, author, license, edit history, and whether
the asset is temporary, generated, purchased, recorded, or original.

## Event Naming

Audio event names should be readable by designers and implementers.

Recommended pattern:

```text
audio.{category}.{context}.{action}
```

Examples:

```text
audio.bgm.forest.enter
audio.sfx.player.pickup
audio.ui.inventory.open
audio.ambience.town.start
```

`game_sound` may propose event names. Final event interfaces must be approved
through `code_interface_contract.md` and implementation review.

## BGM Loop And Transition Rules

BGM proposals must specify:

- Cue purpose
- Emotional target
- Start condition
- Stop condition
- Loop type
- Transition behavior
- Stinger requirements
- Fail-safe behavior when the cue is missing

Loops should avoid obvious fatigue in repeated play. Transition proposals should
state whether music crossfades, cuts, layers, or waits for a musical boundary.

## SFX And UI Sound Rules

SFX and UI sound proposals must specify:

- Trigger condition
- Player feedback purpose
- Event name proposal
- Priority
- Expected repetition rate
- Variation requirement
- Cooldown or anti-spam rule
- Missing-asset fallback

High-frequency sounds require extra review for fatigue, clarity, and mix
priority.

## Ambience Rules

Ambience proposals must specify:

- Region or state
- Layer list
- Day/night or weather variation
- Loop behavior
- Interaction with BGM
- Interaction with gameplay warning cues

Ambience should support play readability and world mood without hiding important
feedback sounds.

## Mix Priority

Default priority from highest to lowest:

1. Critical gameplay warnings
2. Player action feedback
3. UI confirmation and error feedback
4. NPC or quest-relevant cues
5. Environmental danger cues
6. BGM
7. Low-priority ambience

Any exception must be documented in `mix_notes.md` and reviewed by the
Orchestrator.

## Volume And Accessibility

Audio plans should assume separate user controls for:

- Master volume
- BGM volume
- SFX volume
- UI volume
- Ambience volume
- Voice volume if voice is later added

Important gameplay information should not rely on audio alone unless an
equivalent visual or haptic cue is planned.

## License And Provenance

Every proposed asset or reference must record:

- Source
- Author or provider
- License
- Retrieval or acquisition date
- Modification notes
- Usage restrictions
- Whether commercial use is allowed

Unclear provenance blocks promotion into implementation.

## Engine Import Expectations

Before the engine is selected, keep import details engine-neutral.

After engine selection, update this contract or create an engine-specific ADR
covering:

- Supported audio formats
- Import folder layout
- Compression settings
- Loop metadata handling
- Event or bus system
- Runtime loading rules
- Platform-specific constraints
- Automated verification expectations

## Verification Checklist

Before promotion, audio outputs must answer:

- Does this match `game_vision.md`?
- Does it conflict with `narrative_contract.md`, `gameplay_contract.md`, or
  `level_design_contract.md`?
- Are event names only proposals unless implementation has accepted them?
- Are asset names stable and traceable?
- Is provenance complete?
- Are loops and transitions specified for BGM?
- Are priority, variation, and repetition risks specified for SFX?
- Are important gameplay cues accessible without audio-only dependency?
- Are unresolved assumptions labeled?

## Promotion Rules

Audio workstreams may only propose changes through `OUTPUT.md`, `HANDOFF.md`,
`proposed_context_updates.md`, `proposed_adr.md`, and their own artifacts.

The Orchestrator decides whether accepted audio decisions become:

- Contract updates
- ADRs
- PRD changes
- Issues
- Workstream revisions
- Implementation tasks

