from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOT = PROJECT_ROOT / "docs" / "reports"


def _read_optional(path: Path) -> str:
    if not path.exists():
        return "_Missing._"
    return path.read_text(encoding="utf-8", errors="replace").strip() or "_Empty._"


def _render(workstreams: list[str]) -> str:
    sections = []
    for workstream in workstreams:
        folder = PROJECT_ROOT / "workstreams" / workstream
        if not folder.exists():
            folder = PROJECT_ROOT / "workstreams" / "daily_activities" / workstream
        handoff = _read_optional(folder / "HANDOFF.md")
        proposed_context = _read_optional(folder / "proposed_context_updates.md")
        proposed_adr = _read_optional(folder / "proposed_adr.md")
        sections.append(
            f"""## Workstream: `{workstream}`

### Handoff

```md
{handoff}
```

### Proposed Context Updates

```md
{proposed_context}
```

### Proposed ADR

```md
{proposed_adr}
```
"""
        )

    joined = "\n".join(sections)
    return f"""# Merge Preview

Generated for Orchestrator review.

## Scope

- Workstreams: {", ".join(workstreams)}
- Review type: final merge preview

## Workstream Inputs

{joined}

## Orchestrator Decisions

| Proposal | Decision | Reason | Target |
| --- | --- | --- | --- |
|  | accept / revise / reject / user-decision-needed |  |  |

## Conflict Table

| Conflict | Sources | Resolution |
| --- | --- | --- |
|  |  |  |

## Planned File Changes

| File | Change | Requires User Confirmation |
| --- | --- | --- |
|  |  | yes |

## Verification

- Run `scripts/run_quality_gate.ps1`.
- Run the selected engine profile's Game Test Gate if implementation changes are included.
- Update `docs/orchestrator/ORCHESTRATOR_MEMORY.md` or draft a pending memory update.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workstreams", nargs="+")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    text = _render(args.workstreams)
    if args.write:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = "_".join(item.replace("/", "_") for item in args.workstreams)
        target = REPORT_ROOT / f"merge_preview_{safe_name}_{timestamp}.md"
        target.write_text(text, encoding="utf-8")
        print(f"wrote {target.relative_to(PROJECT_ROOT)}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
