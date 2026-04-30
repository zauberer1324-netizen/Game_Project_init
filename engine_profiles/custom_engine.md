# Custom Engine Profile

## Use When

Use this profile when the project intentionally uses a custom runtime, a small
hand-built framework, or an engine not covered by the other profiles.

## Scaffold Direction

Suggested `game_project/` shape after selection:

```text
game_project/
├─ src/
├─ assets/
├─ tests/
├─ tools/
├─ build/
└─ test_config/
```

## Contract Updates

Update `docs/contracts/code_interface_contract.md` with:

- Runtime language and version
- Build command
- Test command
- Module boundaries
- Main loop ownership
- Input model
- Player state type
- Save data shape
- Asset loading rules

## Game Test Gate

Add these checks when this profile is selected:

```powershell
# Replace these with the custom runtime's real commands.
.\scripts\run_game_tests.ps1
.\scripts\run_game_build.ps1
```

Manual verification checklist:

- Runtime starts from a clean checkout.
- Build command is documented.
- Test command is documented.
- A smoke test launches the first scene or simulation.
- First prototype mechanic has a deterministic verification path.
