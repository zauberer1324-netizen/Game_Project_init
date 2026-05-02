# Audio Workstream Architecture Report

## Summary

Added a reusable audio production structure with separate `bgm` and
`game_sound` workstreams.

The audio workstreams are proposal spaces. They do not directly modify central
contracts, accepted game memory, ADRs, PRDs, issues, reports, or
`game_project/`.

## Added Structure

- `docs/contracts/audio_contract.md`
- `workstreams/bgm/`
- `workstreams/game_sound/`

## Role Boundaries

`bgm` owns background music direction proposals, cue sheets, motifs, loops,
transitions, stingers, references, and BGM asset briefs.

`game_sound` owns gameplay SFX proposals, UI audio proposals, ambience
proposals, audio event naming proposals, playback priority, variation, and
verification notes.

`storyline` may propose emotional tone and music needs, but does not own final
BGM or SFX production.

`level_design`, `ui_hud`, and `npc_system` may propose audio needs from their
domains, but final production remains in the audio workstreams and final
promotion remains with the Orchestrator.

## Dependency Source Of Truth

`docs/maps/workstream_dependencies.json` is the source of truth for audio
contract dependencies. Generated maps and `START_PROMPT.md` files should be
regenerated from that JSON whenever dependencies change.

## Guardrail Notes

Audio workstreams may write only inside their assigned folders unless the
Orchestrator explicitly authorizes a different mode.

Audio workstreams should propose central updates through:

- `OUTPUT.md`
- `HANDOFF.md`
- `proposed_context_updates.md`
- `proposed_adr.md`
- workstream-local artifacts, notes, and tests

## Verification

Run the workspace quality gate after regeneration:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1
```

