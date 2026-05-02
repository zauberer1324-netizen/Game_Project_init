from __future__ import annotations

import argparse

from workstream_dependency_lib import PROJECT_ROOT, load_dependency_config


MAP_PATH = PROJECT_ROOT / "docs" / "maps" / "workstream_dependency_map.md"
GRAPH_PATH = PROJECT_ROOT / "docs" / "maps" / "workstream_dependency_graph.mmd"


def _render_map(config: dict) -> str:
    rows = []
    for workstream_id, dependency in config["dependencies"].items():
        label = f"`{workstream_id}/`" if not workstream_id.endswith("/*") else f"`{workstream_id}`"
        contracts = ", ".join(f"`{contract}`" for contract in dependency["contracts"])
        rows.append(f"| {label} | {contracts} | {dependency['why']} |")

    table = "\n".join(rows)
    return f"""# Workstream Dependency Map

This map is generated from `docs/maps/workstream_dependencies.json`.
Edit that JSON file first, then regenerate this document.

## Source Of Truth

- `CONTEXT.md` holds accepted game memory.
- `docs/contracts/*` holds shared constraints.
- `docs/maps/workstream_dependencies.json` is the single source for workstream
  contract dependencies.
- Workstream files are proposals until the Orchestrator accepts them.

## Contract Dependencies

| Workstream | Required Contracts | Why |
| --- | --- | --- |
{table}

## Ownership Boundaries

- `daily_activities/*` owns activity-specific loops, risks, rewards, XP event
  proposals, unlock candidates, and verification notes.
- `progression_system/` owns central skill definitions, XP curves, level
  effects, save data shape, UI display contract, and balance review.
- `level_design/` owns regions, routes, activity placement, resource density,
  risk placement, pacing, and skill-gated location proposals.
- `level_design/` must not own XP formulas or central proficiency curves.
- `bgm/` owns background music direction proposals, cue sheets, motifs, loops,
  transitions, stingers, references, and BGM asset briefs.
- `game_sound/` owns gameplay SFX proposals, UI audio proposals, ambience
  proposals, audio event naming proposals, playback priority, variation, and
  verification notes.
- Audio workstreams may propose sound needs, but the Orchestrator promotes only
  accepted audio decisions into contracts, ADRs, PRDs, issues, or implementation.
- Workstreams must not directly promote proposals into `CONTEXT.md`,
  `docs/contracts/`, `docs/adr/`, `docs/issues/`, or `game_project/`.

## Startup Order Recommendation

1. Run `orchestrator-init`.
2. Fill `game_vision.md`, `gameplay_contract.md`, and the first PRD.
3. Fill `art_direction.md` before serious character or illustration work.
4. Fill `narrative_contract.md` before serious storyline or NPC work.
5. Fill `progression_contract.md` before serious daily activity balancing.
6. Fill `code_interface_contract.md` before code-oriented parallel work.
7. Start only the workstreams marked ready in `docs/orchestrator/ORCHESTRATOR_MEMORY.md`.
"""


def _node_name(value: str) -> str:
    return (
        value.replace("/", "_")
        .replace("*", "ALL")
        .replace("-", "_")
        .replace(".", "_")
        .upper()
    )


def _render_graph(config: dict) -> str:
    lines = ["flowchart TD"]
    declared_contracts: set[str] = set()

    for workstream_id, dependency in config["dependencies"].items():
        workstream_node = _node_name(workstream_id)
        lines.append(f'  {workstream_node}["workstreams/{workstream_id}"]')
        for contract in dependency["contracts"]:
            contract_node = _node_name(contract)
            if contract not in declared_contracts:
                lines.append(f'  {contract_node}["{contract}"]')
                declared_contracts.add(contract)
            lines.append(f"  {contract_node} --> {workstream_node}")

    lines.extend(
        [
            '  DAILY_ACTIVITIES_ALL -. "XP event proposals" .-> PROGRESSION_SYSTEM',
            '  PROGRESSION_SYSTEM -. "skill gates and balance" .-> LEVEL_DESIGN',
            '  LEVEL_DESIGN -. "activity placement" .-> DAILY_ACTIVITIES_ALL',
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    config = load_dependency_config()
    rendered = {
        MAP_PATH: _render_map(config),
        GRAPH_PATH: _render_graph(config),
    }

    if args.write:
        for path, text in rendered.items():
            path.write_text(text, encoding="utf-8")
            print(f"wrote {path.relative_to(PROJECT_ROOT)}")
    else:
        for path, text in rendered.items():
            print(f"\n# {path.relative_to(PROJECT_ROOT)}\n{text}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
