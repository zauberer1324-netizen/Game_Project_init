from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_manifest")
    args = parser.parse_args()

    manifest_path = Path(args.source_manifest)
    sources = json.loads(manifest_path.read_text(encoding="utf-8"))
    if isinstance(sources, dict):
        sources = [sources]

    failures = []
    for source in sources:
        raw_path = ROOT / source.get("raw_path", "")
        if not raw_path.exists():
            failures.append(f"{source.get('source_id', '<missing id>')}: missing {raw_path}")

    if failures:
        print("\n".join(failures))
        return 1

    print("all source raw_path entries exist")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

