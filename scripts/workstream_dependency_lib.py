from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEPENDENCY_PATH = PROJECT_ROOT / "docs" / "maps" / "workstream_dependencies.json"
WORKSTREAM_ROOT = PROJECT_ROOT / "workstreams"

TOP_LEVEL_SKIP = {"_template", "daily_activities"}
DAILY_ACTIVITY_SKIP = {"shared"}


def load_dependency_config() -> dict:
    return json.loads(DEPENDENCY_PATH.read_text(encoding="utf-8"))


def dependency_for(workstream_id: str, config: dict | None = None) -> dict:
    config = config or load_dependency_config()
    dependencies = config["dependencies"]
    if workstream_id in dependencies:
        return dependencies[workstream_id]

    for pattern, dependency in dependencies.items():
        if pattern.endswith("/*"):
            prefix = pattern[:-1]
            if workstream_id.startswith(prefix):
                return dependency

    raise KeyError(f"No dependency mapping for workstream: {workstream_id}")


def workstream_folders() -> list[tuple[str, Path]]:
    folders: list[tuple[str, Path]] = []
    for folder in sorted(WORKSTREAM_ROOT.iterdir()):
        if not folder.is_dir() or folder.name in TOP_LEVEL_SKIP:
            continue
        folders.append((folder.name, folder))

    daily_root = WORKSTREAM_ROOT / "daily_activities"
    if daily_root.exists():
        for folder in sorted(daily_root.iterdir()):
            if not folder.is_dir() or folder.name in DAILY_ACTIVITY_SKIP:
                continue
            folders.append((f"daily_activities/{folder.name}", folder))

    return folders


def contract_paths_for(workstream_id: str, config: dict | None = None) -> list[str]:
    dependency = dependency_for(workstream_id, config)
    root = (config or load_dependency_config()).get("contracts_root", "docs/contracts")
    return [f"{root}/{contract}" for contract in dependency["contracts"]]
