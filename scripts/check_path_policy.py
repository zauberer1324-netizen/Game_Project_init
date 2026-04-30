from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = PROJECT_ROOT / "workspace_policy.json"


def _load_policy() -> dict:
    return json.loads(POLICY_PATH.read_text(encoding="utf-8"))


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
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Unable to read staged files.")
    return [_to_project_path(line) for line in result.stdout.splitlines() if line.strip()]


def _check_workstream(files: list[str], policy: dict, workstream: str | None) -> list[str]:
    if not workstream:
        return ["--workstream is required when --role workstream is used."]

    role = policy["roles"]["workstream"]
    allowed = [
        template.format(workstream=workstream).replace("\\", "/")
        for template in role["allowed_path_templates"]
    ]
    blocked = role["blocked_paths"]
    errors = []

    for path in files:
        if _matches_any(path, blocked):
            errors.append(f"{path}: workstreams may not modify protected central paths.")
        if not _matches_any(path, allowed):
            errors.append(f"{path}: outside allowed workstream folder {allowed}.")

    return errors


def _check_precommit(files: list[str], policy: dict) -> list[str]:
    if not files:
        return []

    role = policy["roles"]["precommit"]
    protected = policy["protected_paths"]
    infrastructure = policy.get("infrastructure_paths", [])
    central_requires = role["central_update_requires_any"]

    central_changes = [
        path
        for path in files
        if _matches_any(path, protected) and not _matches_any(path, infrastructure)
    ]

    if not central_changes:
        return []

    has_review_artifact = any(_matches_any(path, central_requires) for path in files)
    if has_review_artifact:
        return []

    return [
        "Central protected files changed without a review/memory artifact: "
        + ", ".join(central_changes),
        "Stage at least one relevant docs/orchestrator, docs/reports, docs/adr, "
        "docs/prd, docs/issues, or runs artifact with the central change.",
    ]


def _check_required_workstream_outputs(policy: dict) -> list[str]:
    required = policy["workstream_required_outputs"]
    roots = [p for p in (PROJECT_ROOT / "workstreams").iterdir() if p.is_dir()]
    roots.extend(
        p
        for p in (PROJECT_ROOT / "workstreams" / "daily_activities").iterdir()
        if p.is_dir() and p.name not in {"shared"}
    )

    errors = []
    for folder in sorted(set(roots)):
        if folder.name in {"shared", "daily_activities"}:
            continue
        for filename in required:
            if not (folder / filename).exists():
                errors.append(f"{folder.relative_to(PROJECT_ROOT)} missing {filename}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--role", default="precommit", choices=["precommit", "workstream"])
    parser.add_argument("--workstream")
    parser.add_argument("--files", nargs="*", default=[])
    parser.add_argument("--staged", action="store_true")
    parser.add_argument("--check-workstream-outputs", action="store_true")
    args = parser.parse_args()

    policy = _load_policy()
    errors: list[str] = []

    if args.check_workstream_outputs:
        errors.extend(_check_required_workstream_outputs(policy))

    files = [_to_project_path(path) for path in args.files]
    if args.staged:
        try:
            files.extend(_staged_files())
        except RuntimeError as exc:
            print(f"path policy check skipped: {exc}", file=sys.stderr)
            return 1

    files = list(dict.fromkeys(path for path in files if path))

    if args.role == "workstream":
        errors.extend(_check_workstream(files, policy, args.workstream))
    else:
        errors.extend(_check_precommit(files, policy))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("path policy check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
