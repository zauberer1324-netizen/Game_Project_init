from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = PROJECT_ROOT / "orchestrator.config.json"
INDEX_PATH = PROJECT_ROOT / "orchestrator_project" / "context_manager" / "context_index.json"


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _desired_index() -> dict:
    config = _load_json(CONFIG_PATH)
    return {"routes": config["context_routes"]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    if args.check == args.write:
        raise SystemExit("Use exactly one of --check or --write.")

    desired = _desired_index()
    current = _load_json(INDEX_PATH)

    if args.write:
        INDEX_PATH.write_text(json.dumps(desired, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"synced {INDEX_PATH.relative_to(PROJECT_ROOT)}")
        return 0

    if current != desired:
        print("context_index.json differs from orchestrator.config.json context_routes", file=sys.stderr)
        return 1

    print("context index sync check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
