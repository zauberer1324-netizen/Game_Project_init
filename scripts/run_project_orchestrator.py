from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = PROJECT_ROOT / "orchestrator.config.json"
FRAMEWORK_ROOT = PROJECT_ROOT / "orchestrator_project"
sys.path.insert(0, str(FRAMEWORK_ROOT))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from context_manager.select_skill import select_skills


DEFAULT_CONTEXT_ROUTES = {
    "data_analysis": ["CONTEXT.md#Accuracy Rules", "CONTEXT.md#Language"],
    "bug": ["CONTEXT.md#Language", "CONTEXT.md#Game Development Rules"],
    "game_dev": ["CONTEXT.md#Language", "CONTEXT.md#Game Development Rules"],
    "feature": ["CONTEXT.md#Language", "CONTEXT.md#Relationships"],
    "architecture": ["CONTEXT.md#Language", "CONTEXT.md#Relationships"],
    "orchestrator_init": ["AGENTS.md", "CONTEXT.md#Language", "docs/orchestrator/ORCHESTRATOR_MEMORY.md"],
    "workstream_review": ["AGENTS.md", "CONTEXT.md#Language", "docs/orchestrator/ORCHESTRATOR_MEMORY.md"],
    "default": ["CONTEXT.md#Language", "AGENTS.md"],
}


DEFAULT_WORKFLOW_ROUTES = {
    "data_analysis": "workflows/data_analysis.md",
    "bug": "workflows/bug_diagnosis.md",
    "game_dev": "workflows/game_development.md",
    "feature": "workflows/evidence_report.md",
    "architecture": "skills/improve-codebase-architecture/SKILL.md",
    "orchestrator_init": "workflows/orchestrator_init.md",
    "workstream_review": "workflows/workstream_review.md",
}



def _load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return {
        "context_routes": DEFAULT_CONTEXT_ROUTES,
        "workflow_routes": DEFAULT_WORKFLOW_ROUTES,
    }


def _context_routes() -> dict[str, list[str]]:
    return _load_config().get("context_routes", DEFAULT_CONTEXT_ROUTES)


def _workflow_routes() -> dict[str, str]:
    return _load_config().get("workflow_routes", DEFAULT_WORKFLOW_ROUTES)

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


def _load_project_reference(reference: str) -> str:
    file_part, _, section = reference.partition("#")
    path = PROJECT_ROOT / file_part
    text = path.read_text(encoding="utf-8")
    if section:
        text = _extract_heading(text, section)
    return f"\n# FILE: {reference}\n{text}\n"


def _load_project_context(intent: str) -> tuple[list[str], str]:
    routes = _context_routes()
    references = routes.get(intent, routes["default"])
    return references, "\n".join(_load_project_reference(ref) for ref in references)


def _load_workflow(intent: str) -> str:
    relative = _workflow_routes().get(intent, "workflows/evidence_report.md")
    return (FRAMEWORK_ROOT / relative).read_text(encoding="utf-8")


def _load_skills(skill_names: list[str]) -> str:
    chunks = []
    for skill in skill_names:
        path = FRAMEWORK_ROOT / "skills" / skill / "SKILL.md"
        if path.exists():
            chunks.append(f"\n# SKILL: {skill}\n{path.read_text(encoding='utf-8')}")
    return "".join(chunks)


def _build_prompt(
    user_request: str,
    workflow: str,
    selected_context: str,
    selected_skills: list[str],
) -> str:
    return f"""# System Role
You are the Main Orchestrator for the Project_game workspace.

# Workspace Contract
- Use orchestrator_project as the reusable operating framework.
- Use root CONTEXT.md and docs/ as game-specific memory.
- Put actual game code in game_project/.
- Do not write game-specific PRDs, ADRs, or issues into orchestrator_project/.

# Workflow
{workflow}

# Selected Project Context
{selected_context}

# Selected Framework Skills
{_load_skills(selected_skills)}

# User Request
{user_request}

# Mandatory Output
1. Task interpretation
2. Selected workflow
3. Required sub-agents
4. Game-memory updates needed
5. Evidence or verification requirements
6. Execution plan
7. Final answer or next action
8. Strict review when applicable
"""


def _next_run_dir() -> Path:
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    runs_root = PROJECT_ROOT / "runs"
    runs_root.mkdir(exist_ok=True)
    existing = sorted(runs_root.glob(f"{date}_*"))
    run_dir = runs_root / f"{date}_{len(existing) + 1:03d}"
    run_dir.mkdir(parents=True, exist_ok=False)
    return run_dir


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--intent", default="default")
    parser.add_argument("--task-type", default="ambiguous")
    parser.add_argument("--risk", default="low", choices=["low", "medium", "high"])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    context_refs, selected_context = _load_project_context(args.intent)
    selected_skills = select_skills(args.intent, args.task_type, args.risk)
    workflow = _load_workflow(args.intent)
    prompt = _build_prompt(args.request, workflow, selected_context, selected_skills)

    output = {
        "input": args.request,
        "intent": args.intent,
        "task_type": args.task_type,
        "risk": args.risk,
        "selected_context": context_refs,
        "selected_skills": selected_skills,
        "prompt": prompt,
    }

    if args.dry_run:
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0

    run_dir = _next_run_dir()
    (run_dir / "input.md").write_text(args.request, encoding="utf-8")
    (run_dir / "selected_context.json").write_text(
        json.dumps(context_refs, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (run_dir / "selected_skills.json").write_text(
        json.dumps(selected_skills, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (run_dir / "prompt.md").write_text(prompt, encoding="utf-8")
    print(str(run_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())




