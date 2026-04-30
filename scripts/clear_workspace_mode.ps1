$ErrorActionPreference = "Stop"

$script = Join-Path $PSScriptRoot "set_workspace_mode.ps1"
& $script -Mode unlocked
