from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MEMORY_DIR = PROJECT_ROOT / "docs" / "orchestrator"
PENDING_PATH = MEMORY_DIR / "pending_memory_update.md"


def _relative(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")


def _recent_files(patterns: list[str], limit: int = 20) -> list[Path]:
    files: list[Path] = []
    for pattern in patterns:
        files.extend(PROJECT_ROOT.glob(pattern))
    return sorted([p for p in files if p.is_file()], key=lambda p: p.stat().st_mtime, reverse=True)[:limit]


def _workstream_status() -> tuple[list[str], list[str]]:
    ready: list[str] = []
    blocked: list[str] = []
    for brief in sorted((PROJECT_ROOT / "workstreams").glob("*/BRIEF.md")):
        folder = brief.parent
        if folder.name in {"_template", "daily_activities"}:
            continue
        text = brief.read_text(encoding="utf-8", errors="replace").lower()
        if "blocked" in text or "not yet" in text:
            blocked.append(folder.name)
        else:
            ready.append(folder.name)
    for brief in sorted((PROJECT_ROOT / "workstreams" / "daily_activities").glob("*/BRIEF.md")):
        if brief.parent.name == "shared":
            continue
        text = brief.read_text(encoding="utf-8", errors="replace").lower()
        wid = f"daily_activities/{brief.parent.name}"
        if "blocked" in text or "not yet" in text:
            blocked.append(wid)
        else:
            ready.append(wid)
    return ready, blocked


def _render() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    reports = _recent_files(["docs/reports/*.md"])
    decisions = _recent_files(["docs/adr/*.md", "docs/prd/*.md"])
    handoffs = _recent_files(["workstreams/*/HANDOFF.md", "workstreams/daily_activities/*/HANDOFF.md"])
    ready, blocked = _workstream_status()

    report_lines = "\n".join(f"- `{_relative(path)}`" for path in reports) or "- None"
    decision_lines = "\n".join(f"- `{_relative(path)}`" for path in decisions) or "- None"
    handoff_lines = "\n".join(f"- `{_relative(path)}`" for path in handoffs) or "- None"
    ready_lines = "\n".join(f"- `{item}`" for item in ready) or "- None inferred"
    blocked_lines = "\n".join(f"- `{item}`" for item in blocked) or "- None inferred"

    return f"""# Pending Orchestrator Memory Update

Generated at: {now}

This is a draft. The Orchestrator must decide what becomes accepted memory.

## Recent Reports

{report_lines}

## Recent Decisions And PRDs

{decision_lines}

## Recent Handoffs

{handoff_lines}

## Workstreams Possibly Ready

{ready_lines}

## Workstreams Possibly Blocked

{blocked_lines}

## Suggested Memory Update

- Update Current Project Phase if the project moved forward.
- Update Current North Star Summary only if `orchestrator-init` accepted one.
- Add accepted ADRs or PRDs to Accepted Decision Index.
- Add unresolved questions discovered in reports or handoffs.
- Move workstreams between ready and blocked only after Orchestrator review.
- Set Last Orchestration Action to the latest accepted review or initialization.
- Set Next Recommended Orchestration Action to the next concrete step.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    draft = _render()
    if args.write:
        PENDING_PATH.write_text(draft, encoding="utf-8")
        print(f"wrote {PENDING_PATH.relative_to(PROJECT_ROOT)}")
    else:
        print(draft)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
