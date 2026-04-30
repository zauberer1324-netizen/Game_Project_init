from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
WORKSTREAM_ROOT = PROJECT_ROOT / "workstreams"


def _expected_workstream_folders() -> list[Path]:
    folders = [
        path
        for path in WORKSTREAM_ROOT.iterdir()
        if path.is_dir() and path.name not in {"_template", "daily_activities"}
    ]
    daily_root = WORKSTREAM_ROOT / "daily_activities"
    if daily_root.exists():
        folders.extend(
            path
            for path in daily_root.iterdir()
            if path.is_dir() and path.name != "shared"
        )
    return sorted(folders)


def main() -> int:
    problems = []
    for folder in _expected_workstream_folders():
        prompt = folder / "START_PROMPT.md"
        if not prompt.exists():
            problems.append(str(prompt.relative_to(PROJECT_ROOT)))
            continue
        text = prompt.read_text(encoding="utf-8", errors="replace")
        required = ["## Role", "## Read First", "## Work Area", "## Forbidden", "## Required Outputs"]
        for heading in required:
            if heading not in text:
                problems.append(f"{prompt.relative_to(PROJECT_ROOT)} missing {heading}")

    if problems:
        for problem in problems:
            print(problem)
        return 1

    print("start prompt check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
