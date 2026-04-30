#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"

"$PYTHON_BIN" scripts/run_orchestrator.py \
  --request "Check whether Ocrevus is uniquely approved for PPMS" \
  --intent data_analysis \
  --risk high \
  --dry-run >/dev/null

"$PYTHON_BIN" scripts/verify_schema.py \
  schemas/extracted_fact.schema.json \
  examples/extracted_fact.example.json
