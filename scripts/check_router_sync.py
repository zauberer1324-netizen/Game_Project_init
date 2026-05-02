from __future__ import annotations

import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = PROJECT_ROOT / "orchestrator.config.json"
FRAMEWORK_ROOT = PROJECT_ROOT / "orchestrator_project"
INDEX_PATH = FRAMEWORK_ROOT / "context_manager" / "context_index.json"


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _project_reference_exists(reference: str) -> bool:
    file_part = reference.split("#", 1)[0]
    return (PROJECT_ROOT / file_part).exists()


def main() -> int:
    config = _load_json(CONFIG_PATH)
    context_routes = config["context_routes"]
    workflow_routes = config["workflow_routes"]
    required_intents = config.get("required_intents", [])
    framework_index = _load_json(INDEX_PATH)
    framework_routes = framework_index.get("routes", {})
    errors: list[str] = []

    if framework_routes != context_routes:
        errors.append(
            "orchestrator_project/context_manager/context_index.json routes differ from "
            "orchestrator.config.json context_routes. Run scripts/sync_context_index.py --write."
        )

    for intent in required_intents:
        if intent not in context_routes:
            errors.append(f"missing context route for intent: {intent}")
        if intent not in workflow_routes:
            errors.append(f"missing workflow route for intent: {intent}")
        if intent not in framework_routes:
            errors.append(f"framework context_index.json missing route: {intent}")

    for intent, references in context_routes.items():
        for reference in references:
            if not _project_reference_exists(reference):
                errors.append(f"{intent}: missing context reference {reference}")

    for intent, workflow in workflow_routes.items():
        if not (FRAMEWORK_ROOT / workflow).exists():
            errors.append(f"{intent}: missing workflow reference {workflow}")

    sys.path.insert(0, str(FRAMEWORK_ROOT))
    from context_manager.select_skill import select_skills

    init_skills = select_skills("orchestrator_init", "init", "medium")
    review_skills = select_skills("workstream_review", "review", "medium")
    continuity_skills = select_skills("workspace_continuity", "resume", "medium")
    architect_skills = select_skills("project_architect", "project_manager_init", "medium")
    if "orchestrator-init" not in init_skills:
        errors.append("orchestrator_init does not select orchestrator-init")
    if "workstream-review" not in review_skills:
        errors.append("workstream_review does not select workstream-review")
    if "workspace-continuity" not in continuity_skills:
        errors.append("workspace_continuity does not select workspace-continuity")
    if "project-architect" not in architect_skills:
        errors.append("project_architect does not select project-architect")
    if "strict-review" not in init_skills or "strict-review" not in review_skills or "strict-review" not in continuity_skills or "strict-review" not in architect_skills:
        errors.append("medium-risk orchestration routes should select strict-review")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("router sync check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())