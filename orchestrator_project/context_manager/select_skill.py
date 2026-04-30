from __future__ import annotations


def select_skills(intent: str, task_type: str, risk_level: str) -> list[str]:
    skills: list[str] = []

    if intent in {"workspace_continuity", "continuity"} or task_type in {"workspace_continuity", "continuity", "resume", "close"}:
        skills.append("workspace-continuity")

    if intent in {"orchestrator_init", "init"} or task_type in {"orchestrator_init", "init"}:
        skills.append("orchestrator-init")

    if intent in {"workstream_review", "review"} or task_type in {"workstream_review", "review"}:
        skills.append("workstream-review")

    if task_type == "ambiguous":
        skills.append("grill-with-docs")

    if task_type == "feature":
        skills.extend(["to-prd", "to-issues"])

    if task_type == "bug" or intent == "bug":
        skills.append("diagnose")

    if task_type == "implementation":
        skills.append("tdd")

    if task_type == "architecture" or intent == "architecture":
        skills.extend(["zoom-out", "improve-codebase-architecture"])

    if intent == "data_analysis":
        skills.append("grill-with-docs")

    if risk_level in {"medium", "high"}:
        skills.append("strict-review")

    return list(dict.fromkeys(skills))


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument("--intent", default="default")
    parser.add_argument("--task-type", default="ambiguous")
    parser.add_argument("--risk-level", default="low")
    args = parser.parse_args()
    print(json.dumps(select_skills(args.intent, args.task_type, args.risk_level), indent=2))
