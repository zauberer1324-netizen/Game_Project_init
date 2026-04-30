$ErrorActionPreference = "Stop"

$pythonPath = $env:PYTHON_BIN
if (-not $pythonPath) {
  $python = Get-Command python -ErrorAction SilentlyContinue
  if ($python) {
    $pythonPath = $python.Source
  }
}
if (-not $pythonPath) {
  $python = Get-Command py -ErrorAction SilentlyContinue
  if ($python) {
    $pythonPath = $python.Source
  }
}
if (-not $pythonPath) {
  throw "Python executable not found. Install Python or set PYTHON_BIN to an explicit Python path."
}

$env:PYTHON_BIN = $pythonPath
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_quality_gate.ps1