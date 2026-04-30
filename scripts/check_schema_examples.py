from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK_ROOT = PROJECT_ROOT / "orchestrator_project"
SCHEMA_ROOT = FRAMEWORK_ROOT / "schemas"
EXAMPLE_ROOT = FRAMEWORK_ROOT / "examples"
VERIFY_SCHEMA_PATH = FRAMEWORK_ROOT / "scripts" / "verify_schema.py"


def _load_validator():
    spec = importlib.util.spec_from_file_location("verify_schema", VERIFY_SCHEMA_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load verify_schema.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module._validate


def main() -> int:
    validate = _load_validator()
    errors: list[str] = []

    for schema_path in sorted(SCHEMA_ROOT.glob("*.schema.json")):
        example_name = schema_path.name.replace(".schema.json", ".example.json")
        example_path = EXAMPLE_ROOT / example_name
        if not example_path.exists():
            errors.append(f"missing example for {schema_path.name}: {example_name}")
            continue

        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        data = json.loads(example_path.read_text(encoding="utf-8"))
        validation_errors = validate(schema, data)
        for error in validation_errors:
            errors.append(f"{example_name}: {error}")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("schema example check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
