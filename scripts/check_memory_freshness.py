from __future__ import annotations

import argparse
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MEMORY_PATH = PROJECT_ROOT / "docs" / "orchestrator" / "ORCHESTRATOR_MEMORY.md"

REQUIRED_HEADINGS = [
    "## Current Project Phase",
    "## Current North Star Summary",
    "## Accepted Decision Index",
    "## Open Questions",
    "## Workstreams Ready To Start",
    "## Workstreams Blocked",
    "## Last Orchestration Action",
    "## Next Recommended Orchestration Action",
]


def _tracked_state_files() -> list[Path]:
    patterns = [
        "docs/adr/*.md",
        "docs/prd/*.md",
        "docs/reports/*.md",
        "workstreams/*/HANDOFF.md",
        "workstreams/*/proposed_context_updates.md",
        "workstreams/*/proposed_adr.md",
        "workstreams/daily_activities/*/HANDOFF.md",
        "workstreams/daily_activities/*/proposed_context_updates.md",
        "workstreams/daily_activities/*/proposed_adr.md",
    ]
    files: list[Path] = []
    for pattern in patterns:
        files.extend(PROJECT_ROOT.glob(pattern))
    return [path for path in files if path.exists() and path != MEMORY_PATH]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--warn-only", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    if not MEMORY_PATH.exists():
        errors.append("docs/orchestrator/ORCHESTRATOR_MEMORY.md is missing")
    else:
        text = MEMORY_PATH.read_text(encoding="utf-8", errors="replace")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"orchestrator memory missing heading: {heading}")

        memory_mtime = MEMORY_PATH.stat().st_mtime
        newer_files = [
            path
            for path in _tracked_state_files()
            if path.stat().st_mtime > memory_mtime + 1
        ]
        if newer_files:
            formatted = ", ".join(str(path.relative_to(PROJECT_ROOT)) for path in newer_files[:12])
            message = (
                "orchestrator memory may be stale; newer state files exist: "
                + formatted
            )
            if args.warn_only:
                warnings.append(message)
            else:
                errors.append(message)

    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("memory freshness check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
