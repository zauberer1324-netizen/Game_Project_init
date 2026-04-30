from __future__ import annotations

import re
import sys
from pathlib import Path

from workstream_dependency_lib import (
    PROJECT_ROOT,
    contract_paths_for,
    dependency_for,
    load_dependency_config,
    workstream_folders,
)


CONTRACT_LINE_RE = re.compile(r"^- docs/contracts/([A-Za-z0-9_.-]+)\s*$", re.MULTILINE)


def _prompt_contracts(prompt_path: Path) -> list[str]:
    text = prompt_path.read_text(encoding="utf-8", errors="replace")
    start = text.find("## Read First")
    end = text.find("## Dependency Reason")
    if start == -1 or end == -1 or end <= start:
        return CONTRACT_LINE_RE.findall(text)
    return CONTRACT_LINE_RE.findall(text[start:end])


def main() -> int:
    config = load_dependency_config()
    errors: list[str] = []

    for workstream_id, folder in workstream_folders():
        try:
            dependency = dependency_for(workstream_id, config)
        except KeyError as exc:
            errors.append(str(exc))
            continue

        for contract_path in contract_paths_for(workstream_id, config):
            if not (PROJECT_ROOT / contract_path).exists():
                errors.append(f"{workstream_id}: missing contract file {contract_path}")

        prompt_path = folder / "START_PROMPT.md"
        if prompt_path.exists():
            expected = dependency["contracts"]
            actual = _prompt_contracts(prompt_path)
            if actual != expected:
                errors.append(
                    f"{prompt_path.relative_to(PROJECT_ROOT)} contract list mismatch: "
                    f"expected {expected}, got {actual}"
                )

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("workstream dependency check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
