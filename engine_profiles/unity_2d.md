# Unity 2D Engine Profile

## Use When

Use this profile for a 2D game that benefits from Unity's editor workflow,
animation tooling, tilemaps, physics, asset import pipeline, or broader platform
targets.

## Scaffold Direction

Suggested `game_project/` shape after selection:

```text
game_project/
├─ Assets/
│  ├─ Scenes/
│  ├─ Scripts/
│  ├─ Prefabs/
│  ├─ Art/
│  └─ Tests/
├─ Packages/
├─ ProjectSettings/
└─ test_config/
```

## Contract Updates

Update `docs/contracts/code_interface_contract.md` with:

- Unity version
- Render pipeline
- Assembly definition strategy
- Input System choice
- Player state component/interface
- Activity system service/interface
- ScriptableObject usage rules
- Save data shape
- EditMode and PlayMode test expectations

## Game Test Gate

Add these checks when this profile is selected:

```powershell
# Tool availability, adjust Unity path per machine
Unity.exe -quit -batchmode -projectPath .\game_project

# EditMode tests
Unity.exe -quit -batchmode -projectPath .\game_project -runTests -testPlatform EditMode -testResults .\game_project\test_config\editmode-results.xml

# PlayMode tests
Unity.exe -quit -batchmode -projectPath .\game_project -runTests -testPlatform PlayMode -testResults .\game_project\test_config\playmode-results.xml
```

Manual verification checklist:

- First scene opens without missing references.
- Required packages resolve.
- Player prefab exists and can spawn.
- Input bindings are documented.
- Prototype mechanic can be verified in PlayMode.
