$ErrorActionPreference = "Stop"

$pythonPath = $env:PYTHON_BIN
if (-not $pythonPath) {
  $python = (Get-Command python -ErrorAction SilentlyContinue)
  if ($python) {
    $pythonPath = $python.Source
  }
}
if (-not $pythonPath) {
  $python = (Get-Command py -ErrorAction SilentlyContinue)
  if ($python) {
    $pythonPath = $python.Source
  }
}
if (-not $pythonPath) {
  throw "Python executable not found. Install Python or set PYTHON_BIN to an explicit Python path."
}

& $pythonPath .\scripts\run_orchestrator.py --request "Check whether Ocrevus is uniquely approved for PPMS" --intent data_analysis --risk high --dry-run | Out-Null
& $pythonPath .\scripts\verify_schema.py .\schemas\extracted_fact.schema.json .\examples\extracted_fact.example.json
