$ErrorActionPreference = "Stop"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  throw "Git executable not found."
}

if (-not (Test-Path ".git")) {
  git init | Out-Null
}

git config core.hooksPath .githooks
Write-Host "Git hooks installed: core.hooksPath=.githooks"
