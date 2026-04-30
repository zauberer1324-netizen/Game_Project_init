# Engine Profiles

Engine profiles keep this template engine-neutral while making engine selection
actionable.

Use them after `orchestrator-init` chooses or defers an engine.

## Rule

- Before engine selection, keep `game_project/` minimal.
- After engine selection, copy the selected profile's setup and Game Test Gate
  into `game_project/test_config/`.
- Update `docs/contracts/code_interface_contract.md` to match the selected
  engine.
- Add engine-specific build and test commands to the quality process only after
  the engine is selected.

## Available Profiles

- `godot_2d.md`
- `unity_2d.md`
- `phaser_typescript.md`
- `unreal.md`
- `custom_engine.md`
