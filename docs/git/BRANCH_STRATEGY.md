# Branch Strategy

This repository can be used locally only, or connected to GitHub later.

## Recommended Branches

```text
main
├─ orchestrator/init-game-vision
├─ workstream/physics-engine
├─ workstream/character-design
├─ workstream/daily-fishing
└─ integration/prototype-1
```

## Rules

- `main` should represent reviewed and stable project state.
- `workstream/*` branches should stay within their assigned workstream folder.
- `orchestrator/*` branches may update central memory, contracts, PRDs, ADRs, or reports.
- `integration/*` branches combine accepted workstream proposals and implementation changes.
- Do not auto-merge workstream branches into `main`.
