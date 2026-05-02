# Workstreams

Workstreams are isolated workspaces for separate AI chat sessions. Each
workstream should produce a focused result and a compact handoff for the
Orchestrator.

## Rules

1. Read root `AGENTS.md` before starting.
2. Read relevant root `CONTEXT.md` sections.
3. Read relevant `docs/contracts/*` files.
4. Work only inside your assigned workstream unless explicitly authorized.
5. Do not directly edit root `CONTEXT.md`, `docs/contracts/`, or
   `game_project/`.
6. Put final workstream summary in `HANDOFF.md`.
7. Put accepted-change proposals in `proposed_context_updates.md` or
   `proposed_adr.md`.

## Orchestrator Intake Order

The Orchestrator should read `HANDOFF.md` before detailed outputs and artifacts.

## Audio Workstreams

- `bgm/` proposes background music direction, cue sheets, motifs, loops,
  transitions, stingers, references, and BGM asset briefs.
- `game_sound/` proposes gameplay SFX, UI audio, ambience, event naming,
  playback priority, variation, and verification notes.
- Storyline, UI/HUD, level design, and NPC workstreams may request audio needs,
  but accepted audio decisions are promoted by the Orchestrator.

## New Workstream Scaffolding

New workstreams are Project Architect structural changes. Do not create them
inside a specialist workstream chat.

Recommended sequence:

1. Define the new workstream's ownership boundary.
2. Copy or adapt `workstreams/_template/`.
3. Add the dependency entry to `docs/maps/workstream_dependencies.json`.
4. Regenerate derived files:

```powershell
python .\scripts\generate_workstream_dependency_docs.py --write
python .\scripts\generate_workstream_prompts.py --write
```

5. Run the quality gate.
6. Write a structure report and update Orchestrator memory or a pending memory
   update according to the Project Architect memory boundary.

`workstreams/_template/` intentionally does not contain `START_PROMPT.md`.
`START_PROMPT.md` is generated from the dependency map and each workstream's
`BRIEF.md`.
