from __future__ import annotations

import argparse
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MEMORY_PATH = PROJECT_ROOT / "docs" / "orchestrator" / "ORCHESTRATOR_MEMORY.md"
PRD_ROOT = PROJECT_ROOT / "docs" / "prd"


def _section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start == -1:
        return ""
    next_start = text.find("\n## ", start + len(marker))
    if next_start == -1:
        return text[start:]
    return text[start:next_start]


def _has_first_prd() -> bool:
    if not PRD_ROOT.exists():
        return False
    return any(path.name.lower() != "readme.md" for path in PRD_ROOT.glob("*.md"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check whether orchestrator-init has enough recorded output to be considered complete."
    )
    parser.add_argument("--warn-only", action="store_true", help="Print issues but return success.")
    args = parser.parse_args()

    problems: list[str] = []
    if not MEMORY_PATH.exists():
        problems.append("missing docs/orchestrator/ORCHESTRATOR_MEMORY.md")
    else:
        text = MEMORY_PATH.read_text(encoding="utf-8", errors="replace")
        north_star = _section(text, "Current North Star Summary")
        selected_engine = _section(text, "Selected Engine")
        ready = _section(text, "Workstreams Ready To Start")
        blocked = _section(text, "Workstreams Blocked")

        if not north_star or "Not yet defined" in north_star:
            problems.append("Current North Star Summary is not defined.")
        if not selected_engine:
            problems.append("Selected Engine section is missing.")
        elif "Not selected yet" in selected_engine:
            problems.append("Selected Engine is not selected or explicitly deferred.")
        if not ready:
            problems.append("Workstreams Ready To Start section is missing.")
        if not blocked:
            problems.append("Workstreams Blocked section is missing.")

    if not _has_first_prd():
        problems.append("No first PRD exists under docs/prd/.")

    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 0 if args.warn_only else 1

    print("init completion check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
