from __future__ import annotations

import argparse
import json
from pathlib import Path


def _type_matches(expected: str, value: object) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    return True


def _validate(schema: dict, data: object, path: str = "<root>") -> list[str]:
    errors: list[str] = []

    expected_type = schema.get("type")
    if isinstance(expected_type, str) and not _type_matches(expected_type, data):
        return [f"{path}: expected {expected_type}"]

    if "enum" in schema and data not in schema["enum"]:
        errors.append(f"{path}: expected one of {schema['enum']}")

    if isinstance(data, str):
        min_length = schema.get("minLength")
        if min_length is not None and len(data) < min_length:
            errors.append(f"{path}: length must be >= {min_length}")

    if isinstance(data, (int, float)) and not isinstance(data, bool):
        minimum = schema.get("minimum")
        maximum = schema.get("maximum")
        if minimum is not None and data < minimum:
            errors.append(f"{path}: must be >= {minimum}")
        if maximum is not None and data > maximum:
            errors.append(f"{path}: must be <= {maximum}")

    if isinstance(data, list):
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(data):
                errors.extend(_validate(item_schema, item, f"{path}[{index}]"))

    if isinstance(data, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in data:
                errors.append(f"{path}: missing required property '{key}'")

        properties = schema.get("properties", {})
        for key, value in data.items():
            child_path = key if path == "<root>" else f"{path}.{key}"
            if key in properties:
                errors.extend(_validate(properties[key], value, child_path))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{child_path}: additional property not allowed")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("schema")
    parser.add_argument("data")
    args = parser.parse_args()

    schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))
    data = json.loads(Path(args.data).read_text(encoding="utf-8"))
    errors = _validate(schema, data)

    if errors:
        for error in errors:
            print(error)
        return 1

    print("schema validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
