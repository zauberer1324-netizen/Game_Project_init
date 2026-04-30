from __future__ import annotations

import argparse
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _folder_for(workstream: str) -> Path:
    top = PROJECT_ROOT / "workstreams" / workstream
    if top.exists():
        return top
    return PROJECT_ROOT / "workstreams" / "daily_activities" / workstream


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workstreams", nargs="+")
    args = parser.parse_args()

    problems = []
    for workstream in args.workstreams:
        folder = _folder_for(workstream)
        if not folder.exists():
            problems.append(f"missing workstream folder: {workstream}")
            continue
        for filename in ["HANDOFF.md", "OUTPUT.md", "proposed_context_updates.md", "proposed_adr.md"]:
            path = folder / filename
            if not path.exists():
                problems.append(f"{workstream}: missing {filename}")
        handoff = folder / "HANDOFF.md"
        if handoff.exists() and len(handoff.read_text(encoding="utf-8", errors="replace").strip()) < 40:
            problems.append(f"{workstream}: HANDOFF.md appears too sparse for merge review")

    if problems:
        for problem in problems:
            print(problem)
        return 1

    print("merge readiness check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
