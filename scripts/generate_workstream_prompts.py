from __future__ import annotations

import argparse
import json
from pathlib import Path

from workstream_dependency_lib import PROJECT_ROOT, dependency_for, workstream_folders


PROJECT_CONFIG_PATH = PROJECT_ROOT / "orchestrator.config.json"


def _project_name() -> str:
    if not PROJECT_CONFIG_PATH.exists():
        return "Project_game"
    config = json.loads(PROJECT_CONFIG_PATH.read_text(encoding="utf-8"))
    return config.get("project_name", "Project_game")


def _common_header() -> str:
    project_name = _project_name()
    return f"""You are a specialist AI working inside the {project_name} workspace.

Your output is a proposal until the Orchestrator reviews and accepts it.
"""


def _read_brief_summary(folder: Path) -> str:
    brief = folder / "BRIEF.md"
    if not brief.exists():
        return "No BRIEF.md exists yet. Ask the Orchestrator to create one."
    lines = brief.read_text(encoding="utf-8", errors="replace").splitlines()
    return "\n".join(lines[:80]).strip()


def _prompt_for(workstream_id: str, folder: Path) -> str:
    dependency = dependency_for(workstream_id)
    contracts = dependency["contracts"]
    dependency_reason = dependency["why"]
    contract_lines = "\n".join(f"- docs/contracts/{name}" for name in contracts)
    folder_path = str(folder.relative_to(PROJECT_ROOT)).replace("\\", "/")
    brief_summary = _read_brief_summary(folder)

    return f"""# {workstream_id} Start Prompt

{_common_header()}

## Role

You are responsible for the `{workstream_id}` workstream.

## Read First

- AGENTS.md
- CONTEXT.md
- docs/orchestrator/ORCHESTRATOR_MEMORY.md
- docs/maps/workstream_dependency_map.md
{contract_lines}
- {folder_path}/BRIEF.md
- docs/rubrics/handoff_quality_rubric.md

## Dependency Reason

{dependency_reason}

## Work Area

Only edit files inside:

```text
{folder_path}/
```

## Forbidden

- Do not directly edit `CONTEXT.md`.
- Do not directly edit `docs/contracts/`.
- Do not directly edit `docs/adr/`, `docs/prd/`, `docs/issues/`, or `docs/reports/`.
- Do not directly edit `game_project/` unless the Orchestrator explicitly authorizes implementation mode.
- Do not turn assumptions into accepted project facts.

## Required Outputs

- `OUTPUT.md`
- `HANDOFF.md`
- `proposed_context_updates.md`
- `proposed_adr.md`
- artifacts or tests where useful

## Operating Instructions

1. Restate your assigned scope.
2. List the files you read.
3. Identify missing or unresolved contract details before inventing answers.
4. Produce creative or technical work inside your workstream folder.
5. Finish with a compact `HANDOFF.md` for Orchestrator review.
6. Put central-memory suggestions in `proposed_context_updates.md`.
7. Put durable decision suggestions in `proposed_adr.md`.

## Current Brief Snapshot

```md
{brief_summary}
```
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workstream", help="Generate one workstream prompt, e.g. physics_engine or daily_activities/fishing.")
    parser.add_argument("--write", action="store_true", help="Write START_PROMPT.md files.")
    args = parser.parse_args()

    folders = workstream_folders()
    if args.workstream:
        folders = [(wid, folder) for wid, folder in folders if wid == args.workstream]
        if not folders:
            raise SystemExit(f"Unknown workstream: {args.workstream}")

    for workstream_id, folder in folders:
        prompt = _prompt_for(workstream_id, folder)
        target = folder / "START_PROMPT.md"
        if args.write:
            target.write_text(prompt, encoding="utf-8")
            print(f"wrote {target.relative_to(PROJECT_ROOT)}")
        else:
            print(f"\n# {target.relative_to(PROJECT_ROOT)}\n{prompt}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())