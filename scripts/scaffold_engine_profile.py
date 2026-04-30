from __future__ import annotations

import argparse
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROFILE_ROOT = PROJECT_ROOT / "engine_profiles"
GAME_PROJECT = PROJECT_ROOT / "game_project"


def _extract_section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start == -1:
        return ""
    next_start = text.find("\n## ", start + len(marker))
    if next_start == -1:
        return text[start:].strip()
    return text[start:next_start].strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("profile", help="Profile name without .md, e.g. godot_2d")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    profile_path = PROFILE_ROOT / f"{args.profile}.md"
    if not profile_path.exists():
        raise SystemExit(f"Unknown engine profile: {args.profile}")

    text = profile_path.read_text(encoding="utf-8")
    test_gate = _extract_section(text, "Game Test Gate")
    contract_updates = _extract_section(text, "Contract Updates")
    output = f"""# Selected Engine Profile

Selected profile: `{args.profile}`

Source: `engine_profiles/{args.profile}.md`

{contract_updates}

{test_gate}
"""

    target_dir = GAME_PROJECT / "test_config"
    target = target_dir / "GAME_TEST_GATE.md"
    profile_target = GAME_PROJECT / "ENGINE_PROFILE.md"

    if args.write:
        target_dir.mkdir(parents=True, exist_ok=True)
        target.write_text(output, encoding="utf-8")
        profile_target.write_text(f"# Engine Profile\n\nSelected: `{args.profile}`\n\nSee `test_config/GAME_TEST_GATE.md`.\n", encoding="utf-8")
        print(f"wrote {target.relative_to(PROJECT_ROOT)}")
        print(f"wrote {profile_target.relative_to(PROJECT_ROOT)}")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
