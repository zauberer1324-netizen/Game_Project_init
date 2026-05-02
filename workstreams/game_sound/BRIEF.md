# Game Sound Brief

## Mission

Design gameplay SFX, UI audio, ambience, interaction feedback, event naming
proposals, playback priority, variation, and verification notes while preserving
unresolved assumptions.

## Read First

- AGENTS.md
- CONTEXT.md
- docs/orchestrator/ORCHESTRATOR_MEMORY.md
- docs/contracts/game_vision.md
- docs/contracts/gameplay_contract.md
- docs/contracts/audio_contract.md
- docs/contracts/asset_pipeline_contract.md
- docs/contracts/code_interface_contract.md

## Work Area

Work only inside workstreams/game_sound/ unless explicitly authorized.

## Required Outputs

- OUTPUT.md
- HANDOFF.md
- event_table.md
- asset_manifest.md
- reference_notes.md
- mix_notes.md
- proposed_context_updates.md
- proposed_adr.md
- artifacts/ for drafts or structured assets
- tests/ for verification notes

## Forbidden

- Do not directly modify root CONTEXT.md.
- Do not directly modify docs/contracts/.
- Do not directly modify game_project/.
- Do not decide BGM composition, story canon, final event interfaces, or final
  implementation.

## Boundary Notes

This workstream may propose audio event names. Final event interfaces must be
approved through `code_interface_contract.md` and implementation review.

