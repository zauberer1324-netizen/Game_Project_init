from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from context_manager.select_context import load_context, select_context
from context_manager.select_skill import select_skills
from scripts.build_prompt import build_prompt

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def _workflow_for_intent(intent: str) -> str:
    workflow_path = {
        "data_analysis": "workflows/data_analysis.md",
        "bug": "workflows/bug_diagnosis.md",
        "game_dev": "workflows/game_development.md",
        "feature": "workflows/evidence_report.md",
        "architecture": "skills/improve-codebase-architecture/SKILL.md",
        "orchestrator_init": "workflows/orchestrator_init.md",
        "workstream_review": "workflows/workstream_review.md",
    }.get(intent, "workflows/evidence_report.md")
    return (ROOT / workflow_path).read_text(encoding="utf-8")


def _next_run_dir() -> Path:
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    runs_root = ROOT / "runs"
    runs_root.mkdir(exist_ok=True)
    existing = sorted(runs_root.glob(f"{date}_*"))
    next_num = len(existing) + 1
    run_dir = runs_root / f"{date}_{next_num:03d}"
    run_dir.mkdir(parents=True, exist_ok=False)
    (run_dir / "agent_outputs").mkdir()
    return run_dir


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--intent", default="default")
    parser.add_argument("--task-type", default="ambiguous")
    parser.add_argument("--risk", default="low", choices=["low", "medium", "high"])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    context_refs = select_context(args.intent)
    selected_context = load_context(args.intent)
    selected_skills = select_skills(args.intent, args.task_type, args.risk)
    workflow = _workflow_for_intent(args.intent)
    prompt = build_prompt(args.request, selected_context, selected_skills, workflow)

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
