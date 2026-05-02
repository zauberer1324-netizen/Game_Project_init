param(
  [Parameter(Mandatory=$true)]
  [ValidateSet("unlocked", "workstream", "orchestrator-proposal", "orchestrator-apply", "implementation", "project-architect-proposal", "project-architect-apply")]
  [string]$Mode,

  [string]$Workstream,
  [string]$Approval
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$PolicyPath = Join-Path $ProjectRoot "workspace_policy.json"
$GuardDir = Join-Path $ProjectRoot ".workspace_guard"
$ModePath = Join-Path $GuardDir "mode.json"

function Convert-ToProjectPath {
  param([Parameter(Mandatory=$true)][string]$Path)
  $full = [System.IO.Path]::GetFullPath($Path)
  $root = [System.IO.Path]::GetFullPath($ProjectRoot).TrimEnd("\") + "\"
  if (-not $full.StartsWith($root, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Path is outside project root: $Path"
  }
  $relative = $full.Substring($root.Length)
  return $relative.Replace("\", "/")
}

function Test-MatchesRule {
  param(
    [Parameter(Mandatory=$true)][string]$Path,
    [Parameter(Mandatory=$true)][string]$Rule
  )
  $rule = $Rule.Replace("\", "/")
  if ($rule -eq "*") { return $true }
  if ($rule.EndsWith("/")) { return $Path.StartsWith($rule) }
  return $Path -eq $rule
}

function Test-MatchesAny {
  param(
    [Parameter(Mandatory=$true)][string]$Path,
    [Parameter(Mandatory=$true)][string[]]$Rules
  )
  foreach ($rule in $Rules) {
    if (Test-MatchesRule -Path $Path -Rule $rule) { return $true }
  }
  return $false
}

function Unlock-PreviousMode {
  if (-not (Test-Path $ModePath)) { return }
  $previous = Get-Content -LiteralPath $ModePath -Raw -Encoding UTF8 | ConvertFrom-Json
  if (-not $previous.locked_files) { return }
  foreach ($relative in $previous.locked_files) {
    $file = Join-Path $ProjectRoot $relative
    if (Test-Path -LiteralPath $file -PathType Leaf) {
      Set-ItemProperty -LiteralPath $file -Name IsReadOnly -Value $false
    }
  }
}

function Resolve-AllowedPaths {
  param([Parameter(Mandatory=$true)]$ModeConfig)
  $allowed = @()
  if ($ModeConfig.allowed_write_paths) {
    $allowed += @($ModeConfig.allowed_write_paths)
  }
  if ($ModeConfig.allowed_path_templates) {
    foreach ($template in @($ModeConfig.allowed_path_templates)) {
      if (-not $Workstream) {
        throw "Mode '$Mode' requires -Workstream."
      }
      $allowed += $template.Replace("{workstream}", $Workstream).Replace("\", "/")
    }
  }
  if (-not $allowed) { $allowed = @("*") }
  return @($allowed)
}

New-Item -ItemType Directory -Force -Path $GuardDir | Out-Null
$policy = Get-Content -LiteralPath $PolicyPath -Raw -Encoding UTF8 | ConvertFrom-Json
$modeConfig = $policy.workspace_modes.$Mode
if (-not $modeConfig) {
  throw "Mode '$Mode' is not defined in workspace_policy.json."
}

if ($modeConfig.requires_workstream -and -not $Workstream) {
  throw "Mode '$Mode' requires -Workstream."
}
if ($modeConfig.requires_approval -and -not $Approval) {
  throw "Mode '$Mode' requires -Approval."
}

Unlock-PreviousMode

$allowed = Resolve-AllowedPaths -ModeConfig $modeConfig
$locked = @()
$lockScope = $modeConfig.lock_scope

if ($lockScope -eq "all_except_allowed") {
  $files = Get-ChildItem -LiteralPath $ProjectRoot -Recurse -File -Force |
    Where-Object {
      $relative = Convert-ToProjectPath -Path $_.FullName
      -not $relative.StartsWith(".git/") -and
      -not $relative.StartsWith(".workspace_guard/")
    }

  foreach ($file in $files) {
    $relative = Convert-ToProjectPath -Path $file.FullName
    if (-not (Test-MatchesAny -Path $relative -Rules $allowed)) {
      Set-ItemProperty -LiteralPath $file.FullName -Name IsReadOnly -Value $true
      $locked += $relative
    }
  }
}

$state = [ordered]@{
  mode = $Mode
  workstream = $Workstream
  approval = $Approval
  allowed_write_paths = $allowed
  lock_strategy = "read-only"
  lock_scope = $lockScope
  locked_files = $locked
  started_at = (Get-Date).ToUniversalTime().ToString("o")
}

$modeJson = $state | ConvertTo-Json -Depth 20
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($ModePath, $modeJson + [Environment]::NewLine, $utf8NoBom)
Write-Host "workspace mode set: $Mode"
Write-Host "allowed write paths: $($allowed -join ', ')"
Write-Host "read-only locked files: $($locked.Count)"
