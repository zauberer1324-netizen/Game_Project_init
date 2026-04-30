from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROFILE_ROOT = PROJECT_ROOT / "engine_profiles"
REQUIRED = ["## Use When", "## Scaffold Direction", "## Contract Updates", "## Game Test Gate"]


def main() -> int:
    profiles = [path for path in PROFILE_ROOT.glob("*.md") if path.name != "README.md"]
    problems = []
    if not profiles:
        problems.append("no engine profiles found")
    for profile in profiles:
        text = profile.read_text(encoding="utf-8", errors="replace")
        for heading in REQUIRED:
            if heading not in text:
                problems.append(f"{profile.relative_to(PROJECT_ROOT)} missing {heading}")

    if problems:
        for problem in problems:
            print(problem)
        return 1

    print("engine profile check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
