# Workspace Guard Implementation Report

## Scope

Added optional accidental-write protection without Windows ACL hard locks.

## Added

- `.workspace_guard/.gitkeep`
- `scripts/set_workspace_mode.ps1`
- `scripts/clear_workspace_mode.ps1`
- `scripts/check_workspace_mode.py`
- `docs/guides/workspace_guard.md`

## Updated

- `workspace_policy.json` now defines workspace modes.
- `.gitignore` ignores runtime guard state while preserving `.workspace_guard/.gitkeep`.
- `.githooks/pre-commit` checks workspace mode before path policy.
- `scripts/run_quality_gate.ps1` checks workspace mode when inside a Git repo.
- `AGENTS.md`, `README.md`, `docs/USER_GUIDE.md`, and
  `docs/guides/workspace_continuity.md` reference the guard.

## Modes

- `unlocked`
- `workstream`
- `orchestrator-proposal`
- `orchestrator-apply`
- `implementation`

## Validation

Manual behavior check:

- `workstream` mode allowed `workstreams/physics_engine/HANDOFF.md`.
- `workstream` mode rejected `CONTEXT.md`.
- `clear_workspace_mode.ps1` returned the workspace to `unlocked`.
- `orchestrator-apply` without `-Approval` failed as expected.

Quality gate result:

```text
context index sync check passed
router sync check passed
schema example check passed
memory freshness check passed
path policy check passed
workstream dependency check passed
start prompt check passed
engine profile check passed
workspace mode check passed (unlocked)
path policy check passed
quality gate passed
```

## Remaining Limitations

This is a soft guard, not hostile-code security. It uses read-only file
attributes and Git checks, not ACL deny rules. A process running as the same
Windows user can still remove read-only attributes if instructed to do so.
