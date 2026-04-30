# Accuracy-Grounded Orchestrator

This project is a scaffold for a context-controlled, evidence-grounded AI
orchestration workflow.

The main idea is simple: the Orchestrator should not ingest bulk raw material
directly. Raw sources are stored under `data/raw/`, extracted into atomic facts,
verified against source locations, reviewed for conflicts, and only then used in
the final answer.

## Workflow

1. Classify the user request.
2. Select only the needed context and skills.
3. Assign narrow tasks to sub-agents.
4. Store raw evidence and structured outputs.
5. Validate schemas.
6. Verify claims against evidence.
7. Run strict review.
8. Produce the final answer.

## Important Paths

- `AGENTS.md` - operating rules for the main orchestrator.
- `CONTEXT.md` - domain language and accuracy rules.
- `workflows/` - task-specific workflow guidance.
- `skills/` - reusable agent skills.
- `context_manager/` - context and skill routing helpers.
- `agents/` - sub-agent role prompts.
- `schemas/` - JSON schemas for evidence and reports.
- `data/` - raw, extracted, verified, and rejected artifacts.
- `runs/` - per-run logs and outputs.

## Quick Check

Run schema and routing checks:

```powershell
python .\scripts\run_orchestrator.py --request "Check whether Ocrevus is uniquely approved for PPMS" --intent data_analysis --risk high --dry-run
python .\scripts\verify_schema.py .\schemas\extracted_fact.schema.json .\examples\extracted_fact.example.json
```

On Windows, if PowerShell blocks `.ps1` scripts or Python is not on `PATH`, run:

```powershell
$env:PYTHON_BIN="C:\Path\To\python.exe"
powershell -ExecutionPolicy Bypass -File .\scripts\run_tests.ps1
```
