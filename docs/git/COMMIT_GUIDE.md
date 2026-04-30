# Commit Guide

## Commit Shape

Use small commits that describe the project operation or game feature clearly.

Examples:

```text
Initialize game vision contracts
Add physics workstream handoff
Review fishing activity proposal
Scaffold Phaser TypeScript prototype
```

## Before Commit

Run:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1
```

If implementation changed, also run the selected engine profile's Game Test Gate
from `game_project/test_config/GAME_TEST_GATE.md`.
