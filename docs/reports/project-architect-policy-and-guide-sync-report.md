# Project Architect Policy And Guide Sync Report

## Summary

Updated the user-facing guide and Project Architect path policy so the current
workspace structure matches the intended operating model.

## Changes

- Added a latest-structure section to `docs/USER_GUIDE.md` covering:
  - engine selection or deferral during `orchestrator-init`
  - `Selected Engine` memory usage
  - audio workstreams and `audio_contract.md`
  - Project Architect workspace identity/reset tooling
  - workstream scaffolding tooling
  - `scripts/README.md`, `data/`, and `runs/`
  - recommended startup prompts
- Expanded `workspace_policy.json` so Project Architect apply mode can edit
  structural user-facing documents such as root README files, startup guides,
  `docs/USER_GUIDE.md`, README files under PRD/issues/data/runs, and
  `docs/agents/`.
- Left the Project Architect memory exception rule unchanged.

## Verification

Run the standard quality gate after this sync.
