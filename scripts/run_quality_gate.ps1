$ErrorActionPreference = "Stop"
$env:PYTHONDONTWRITEBYTECODE = "1"

function Invoke-StepQuiet {
  param(
    [Parameter(Mandatory=$true)][string]$FilePath,
    [Parameter(ValueFromRemainingArguments=$true)][string[]]$StepArgs
  )

  & $FilePath @StepArgs | Out-Null
  if ($LASTEXITCODE -ne 0) {
    throw "Command failed with exit code ${LASTEXITCODE}: $FilePath $($StepArgs -join ' ')"
  }
}

function Invoke-Step {
  param(
    [Parameter(Mandatory=$true)][string]$FilePath,
    [Parameter(ValueFromRemainingArguments=$true)][string[]]$StepArgs
  )

  & $FilePath @StepArgs
  if ($LASTEXITCODE -ne 0) {
    throw "Command failed with exit code ${LASTEXITCODE}: $FilePath $($StepArgs -join ' ')"
  }
}

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

Invoke-Step $pythonPath .\scripts\sync_context_index.py --check
Invoke-Step $pythonPath .\scripts\check_router_sync.py
Invoke-Step $pythonPath .\scripts\check_schema_examples.py
Invoke-Step $pythonPath .\scripts\check_memory_freshness.py --warn-only
Invoke-Step $pythonPath .\scripts\check_path_policy.py --check-workstream-outputs
Invoke-Step $pythonPath .\scripts\check_workstream_dependencies.py
Invoke-Step $pythonPath .\scripts\check_start_prompts.py
Invoke-Step $pythonPath .\scripts\check_engine_profiles.py
$projectName = "Project_game"
if (Test-Path .\orchestrator.config.json) {
  $projectConfig = Get-Content -Path .\orchestrator.config.json -Raw | ConvertFrom-Json
  if ($projectConfig.project_name) {
    $projectName = $projectConfig.project_name
  }
}
Invoke-StepQuiet $pythonPath .\scripts\initialize_from_template.py --project-name $projectName
Invoke-StepQuiet $pythonPath .\scripts\draft_memory_update.py
Invoke-StepQuiet $pythonPath .\scripts\build_merge_preview.py physics_engine
Invoke-StepQuiet $pythonPath .\scripts\run_project_orchestrator.py --request "Initialize game direction" --intent orchestrator_init --task-type init --risk medium --dry-run
Invoke-StepQuiet $pythonPath .\scripts\run_project_orchestrator.py --request "Review a workstream handoff" --intent workstream_review --task-type review --risk medium --dry-run
Invoke-StepQuiet $pythonPath .\scripts\run_project_orchestrator.py --request "Recover workspace state" --intent workspace_continuity --task-type resume --risk medium --dry-run

$insideGit = $false
try {
  git rev-parse --is-inside-work-tree 2>$null | Out-Null
  if ($LASTEXITCODE -eq 0) {
    $insideGit = $true
  }
} catch {
  $insideGit = $false
}
if ($insideGit) {
  Invoke-Step $pythonPath .\scripts\check_workspace_mode.py --staged
  Invoke-Step $pythonPath .\scripts\check_path_policy.py --staged --role precommit
}

Write-Host "quality gate passed"