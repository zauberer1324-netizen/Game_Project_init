"""Workspace identity/reset tool managed by the Project Architect.

Use this script when the current workspace needs project-name replacement,
runtime folder cleanup, or a compact Orchestrator memory reset. This is not the
standard user flow after a fresh clone, and it is not a workstream scaffolding
tool. New or changed workstreams should be handled through `workstreams/_template/`,
`docs/maps/workstream_dependencies.json`, and the workstream generation scripts.
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_CONFIG = PROJECT_ROOT / "template.config.json"


def _load_template_config() -> dict:
    return json.loads(TEMPLATE_CONFIG.read_text(encoding="utf-8"))


def _replace_in_file(path: Path, old: str, new: str, apply: bool) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    updated = text.replace(old, new)
    if updated == text:
        return False
    if apply:
        path.write_text(updated, encoding="utf-8")
    return True


def _safe_clear_folder(path: Path, apply: bool) -> list[str]:
    cleared: list[str] = []
    if not path.exists():
        return cleared
    root = PROJECT_ROOT.resolve()
    target = path.resolve()
    if root not in target.parents and target != root:
        raise RuntimeError(f"Refusing to clear outside project root: {path}")
    for child in path.iterdir():
        if child.name == ".gitkeep":
            continue
        cleared.append(str(child.relative_to(PROJECT_ROOT)))
        if apply:
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    if apply:
        (path / ".gitkeep").touch(exist_ok=True)
    return cleared


def _reset_memory(project_name: str, apply: bool) -> bool:
    path = PROJECT_ROOT / "docs" / "orchestrator" / "ORCHESTRATOR_MEMORY.md"
    text = f"""# Orchestrator Memory

This file is the Orchestrator's compact operational memory for `{project_name}`.
It is not the source of truth. Accepted game rules belong in `CONTEXT.md`.
Shared constraints belong in `docs/contracts/`. Durable decisions belong in
`docs/adr/`.

## Current Project Phase

Template initialized for a new game. Game-specific vision still needs
user-guided initialization.

## Current North Star Summary

Not yet defined. Run `orchestrator-init` before starting specialist workstreams.

## Accepted Decision Index

- No game-specific decisions accepted yet.

## Open Questions

- What is the one-sentence game pitch?
- What is the core player fantasy?
- What is the first playable prototype scope?
- Which engine profile should be selected, if any?

## Workstreams Ready To Start

None. Run `orchestrator-init` first.

## Workstreams Blocked

- All workstreams are blocked on initial game direction.

## Last Orchestration Action

Initialized template metadata for `{project_name}`.

## Next Recommended Orchestration Action

Run `orchestrator-init` with the user.
"""
    if apply:
        path.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--apply", action="store_true", help="Apply changes. Without this flag, print a dry run.")
    parser.add_argument("--clear-runtime", action="store_true", help="Clear runs and data folders listed in template.config.json.")
    parser.add_argument("--reset-memory", action="store_true", help="Reset Orchestrator memory for the new game.")
    args = parser.parse_args()

    config = _load_template_config()
    old_name = config.get("replaceable_project_name", "Project_game")
    changed: list[str] = []

    for relative in ["README.md", "CONTEXT.md", "AGENTS.md", "orchestrator.config.json"]:
        path = PROJECT_ROOT / relative
        if _replace_in_file(path, old_name, args.project_name, args.apply):
            changed.append(relative)

    config_path = PROJECT_ROOT / "orchestrator.config.json"
    if config_path.exists():
        config_data = json.loads(config_path.read_text(encoding="utf-8"))
        if config_data.get("project_name") != args.project_name:
            changed.append("orchestrator.config.json:project_name")
            if args.apply:
                config_data["project_name"] = args.project_name
                config_path.write_text(json.dumps(config_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.reset_memory:
        _reset_memory(args.project_name, args.apply)
        changed.append("docs/orchestrator/ORCHESTRATOR_MEMORY.md")

    cleared: list[str] = []
    if args.clear_runtime:
        for relative in config.get("reset_on_new_game", []):
            cleared.extend(_safe_clear_folder(PROJECT_ROOT / relative, args.apply))

    mode = "applied" if args.apply else "dry-run"
    print(f"template initialization {mode}")
    for item in changed:
        print(f"would update: {item}" if not args.apply else f"updated: {item}")
    for item in cleared:
        print(f"would clear: {item}" if not args.apply else f"cleared: {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
