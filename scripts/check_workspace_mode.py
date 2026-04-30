from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GUARD_DIR = PROJECT_ROOT / ".workspace_guard"
MODE_PATH = GUARD_DIR / "mode.json"


def _to_project_path(path: str) -> str:
    raw = Path(path)
    try:
        if raw.is_absolute():
            raw = raw.resolve().relative_to(PROJECT_ROOT)
    except ValueError:
        pass
    normalized = str(raw).replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def _matches(path: str, rule: str) -> bool:
    rule = rule.replace("\\", "/")
    if rule == "*":
        return True
    if rule.endswith("/"):
        return path.startswith(rule)
    return path == rule


def _matches_any(path: str, rules: list[str]) -> bool:
    return any(_matches(path, rule) for rule in rules)


def _staged_files() -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMRD"],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Unable to read staged files.")
    return [_to_project_path(line) for line in result.stdout.splitlines() if line.strip()]


def _load_mode() -> dict:
    if not MODE_PATH.exists():
        return {
            "mode": "unlocked",
            "allowed_write_paths": ["*"],
            "locked_files": [],
        }
    return json.loads(MODE_PATH.read_text(encoding="utf-8-sig"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--staged", action="store_true")
    parser.add_argument("--files", nargs="*", default=[])
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()

    mode = _load_mode()
    mode_name = mode.get("mode", "unlocked")
    allowed = mode.get("allowed_write_paths", ["*"])
    if isinstance(allowed, str):
        allowed = [allowed]

    if args.show:
        print(json.dumps(mode, ensure_ascii=False, indent=2))
        return 0

    files = [_to_project_path(path) for path in args.files]
    if args.staged:
        try:
            files.extend(_staged_files())
        except RuntimeError as exc:
            print(f"workspace mode check skipped: {exc}", file=sys.stderr)
            return 1

    files = list(dict.fromkeys(path for path in files if path))
    if not files:
        print(f"workspace mode check passed ({mode_name})")
        return 0

    if mode_name == "unlocked" or _matches_any("*", allowed):
        print(f"workspace mode check passed ({mode_name})")
        return 0

    errors = [
        f"{path}: outside allowed write paths for mode {mode_name}: {allowed}"
        for path in files
        if not _matches_any(path, allowed)
    ]

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"workspace mode check passed ({mode_name})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
