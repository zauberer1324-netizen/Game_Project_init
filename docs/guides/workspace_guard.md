# Workspace Guard Guide

Workspace Guard adds an optional, reversible safety layer around the existing
prompt rules, path policy, quality gate, and Git hooks.

It does not use Windows ACL hard locks. It uses:

- workspace modes
- read-only file attributes for soft locking
- pre-commit mode checks
- quality-gate checks

## Modes

| Mode | Use When | Writable Paths |
| --- | --- | --- |
| `unlocked` | Normal flexible work | All paths |
| `workstream` | A specialist workstream chat is active | `workstreams/<name>/` |
| `orchestrator-proposal` | Orchestrator is reviewing before user approval | `docs/reports/`, `runs/`, `docs/orchestrator/pending_memory_update.md` |
| `orchestrator-apply` | User has approved central integration | All paths |
| `implementation` | Approved game implementation work | `game_project/`, `docs/issues/`, `docs/reports/`, `runs/` |

## Workstream Mode

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\set_workspace_mode.ps1 -Mode workstream -Workstream physics_engine
```

This marks files outside `workstreams/physics_engine/` as read-only and records
the active mode in `.workspace_guard/mode.json`.

Clear the mode:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\clear_workspace_mode.ps1
```

## Orchestrator Proposal Mode

Use this before a review where central files should not be changed yet.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\set_workspace_mode.ps1 -Mode orchestrator-proposal
```

The Orchestrator may write reports and proposal artifacts, but central memory,
contracts, PRDs, ADRs, and `game_project/` stay soft-locked.

## Orchestrator Apply Mode

Use this only after the user explicitly approves applying changes.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\set_workspace_mode.ps1 -Mode orchestrator-apply -Approval "user-confirmed"
```

## Implementation Mode

Use this for approved implementation work under `game_project/`.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\set_workspace_mode.ps1 -Mode implementation
```

## Check Current Mode

```powershell
$env:PYTHON_BIN = "C:\Users\이중원\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
& $env:PYTHON_BIN .\scripts\check_workspace_mode.py --show
```

## Limitations

This is a safety guard, not hostile-code security.

Because Codex and other tools run as the same Windows user, they can technically
remove read-only attributes if instructed to do so. The value of this guard is
that accidental edits fail earlier, and staged files are still checked before
commit.
