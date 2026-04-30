from __future__ import annotations

import json
import re
from pathlib import Path


FRAMEWORK_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = FRAMEWORK_ROOT.parent
PROJECT_CONFIG_PATH = PROJECT_ROOT / "orchestrator.config.json"
INDEX_PATH = FRAMEWORK_ROOT / "context_manager" / "context_index.json"


def _using_project_config() -> bool:
    return PROJECT_CONFIG_PATH.exists()


def _reference_root() -> Path:
    return PROJECT_ROOT if _using_project_config() else FRAMEWORK_ROOT


def _load_routes() -> dict[str, list[str]]:
    if _using_project_config():
        return json.loads(PROJECT_CONFIG_PATH.read_text(encoding="utf-8"))["context_routes"]
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))["routes"]


def select_context(intent: str) -> list[str]:
    routes = _load_routes()
    return routes.get(intent, routes["default"])


def _extract_heading(text: str, heading: str) -> str:
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return text

    start = match.start()
    next_heading = re.search(r"^##\s+", text[match.end() :], re.MULTILINE)
    if not next_heading:
        return text[start:].strip()
    end = match.end() + next_heading.start()
    return text[start:end].strip()


def load_reference(reference: str) -> str:
    file_part, _, section = reference.partition("#")
    path = _reference_root() / file_part
    text = path.read_text(encoding="utf-8")
    if section:
        text = _extract_heading(text, section)
    return f"\n# FILE: {reference}\n{text}\n"


def load_context(intent: str) -> str:
    return "\n".join(load_reference(ref) for ref in select_context(intent))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("intent")
    args = parser.parse_args()
    print(load_context(args.intent))