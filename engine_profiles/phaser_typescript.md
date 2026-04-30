# Phaser TypeScript Engine Profile

## Use When

Use this profile for a browser-first 2D prototype or game where fast iteration,
web deployment, TypeScript tests, and Playwright verification are useful.

## Scaffold Direction

Suggested `game_project/` shape after selection:

```text
game_project/
├─ package.json
├─ tsconfig.json
├─ vite.config.ts
├─ src/
│  ├─ main.ts
│  ├─ scenes/
│  ├─ systems/
│  └─ assets/
├─ tests/
├─ e2e/
└─ test_config/
```

## Contract Updates

Update `docs/contracts/code_interface_contract.md` with:

- Phaser version
- TypeScript strictness
- Scene lifecycle rules
- Input event naming
- Player state type
- Activity system module boundary
- Save data type
- Unit and browser test expectations

## Game Test Gate

Add these checks when this profile is selected:

```powershell
cd .\game_project
npm install
npm run typecheck
npm test
npm run build
npx playwright test
```

Manual verification checklist:

- Dev server starts.
- Canvas is nonblank.
- Main scene loads.
- Keyboard or pointer input works.
- First prototype mechanic has unit or Playwright coverage.
