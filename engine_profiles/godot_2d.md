# Godot 2D Engine Profile

## Use When

Use this profile for a lightweight 2D game where scenes, nodes, signals, and
fast iteration are more important than heavy production tooling.

## Scaffold Direction

Suggested `game_project/` shape after selection:

```text
game_project/
├─ project.godot
├─ scenes/
├─ scripts/
├─ assets/
├─ tests/
└─ test_config/
```

## Contract Updates

Update `docs/contracts/code_interface_contract.md` with:

- Godot version
- GDScript or C# choice
- Scene ownership rules
- Signal naming rules
- Player state node/interface
- Activity system autoload/interface
- Save data resource or JSON shape
- Test runner approach

## Game Test Gate

Add these checks when this profile is selected:

```powershell
# Tool availability
godot --version

# Project opens headlessly
godot --headless --path .\game_project --quit

# Optional, if a test runner plugin or script is installed
godot --headless --path .\game_project -s res://tests/run_tests.gd
```

Manual verification checklist:

- Main scene opens without missing resources.
- Player input is detected.
- A minimal scene can load, run, and exit.
- Save/load path is known, even if not implemented.
- First prototype mechanic has a repeatable verification checklist.
