# Unreal Engine Profile

## Use When

Use this profile for a larger 3D or high-fidelity 2D/2.5D game where Unreal's
rendering, animation, behavior trees, world tooling, or C++/Blueprint workflow is
important enough to justify heavier setup.

## Scaffold Direction

Suggested `game_project/` shape after selection:

```text
game_project/
├─ Config/
├─ Content/
├─ Source/
├─ Tests/
├─ ProjectName.uproject
└─ test_config/
```

## Contract Updates

Update `docs/contracts/code_interface_contract.md` with:

- Unreal version
- Blueprint vs C++ boundary
- Module layout
- Player state class/interface
- Activity system component/interface
- SaveGame object shape
- Automation test expectations
- Asset naming and content folder rules

## Game Test Gate

Add these checks when this profile is selected:

```powershell
# Adjust UnrealEditor-Cmd path per machine
UnrealEditor-Cmd.exe .\game_project\ProjectName.uproject -run=Automation -unattended -nop4

# Optional packaged build check, adjust platform as needed
RunUAT.bat BuildCookRun -project=.\game_project\ProjectName.uproject -noP4 -build -cook -stage -pak -clientconfig=Development
```

Manual verification checklist:

- Project opens without missing plugins.
- Default map loads.
- Player pawn can spawn.
- Input mapping context or project input settings are documented.
- First prototype mechanic has an automation or manual verification path.
