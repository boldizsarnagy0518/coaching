<#
.SYNOPSIS
    Registers a daily Windows scheduled task that runs a verified database backup.

.DESCRIPTION
    Runs `uv run python manage.py backup_db` in the project folder every day at -Time.
    With -CopyTo, the newest backup is also copied to that folder (for example a synced
    OneDrive folder or an external drive), so a disk failure does not take both copies.
    Run it yourself in PowerShell; it only affects the current user's task list.
    Remove the task with: Unregister-ScheduledTask -TaskName CoachingBackup

.EXAMPLE
    .\scripts\register-backup-task.ps1 -Time 21:30 -CopyTo "$env:OneDrive\CoachingBackups"
#>
param(
    [string]$Time = "21:00",
    [int]$Keep = 14,
    [string]$CopyTo = "",
    [string]$TaskName = "CoachingBackup"
)

$ErrorActionPreference = "Stop"
$project = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$uv = (Get-Command uv).Source

$command = "Set-Location '$project'; & '$uv' run python manage.py backup_db --keep $Keep"
if ($CopyTo) {
    $command += "; if (`$LASTEXITCODE -eq 0) { New-Item -ItemType Directory -Force '$CopyTo' | Out-Null; " +
        "Get-ChildItem '$project\.local\backups\db-*.sqlite3' | Sort-Object LastWriteTime | Select-Object -Last 1 | " +
        "Copy-Item -Destination '$CopyTo' }"
}

$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -NonInteractive -Command `"$command`""
$trigger = New-ScheduledTaskTrigger -Daily -At $Time
# StartWhenAvailable: run at the next opportunity if the computer was off at the scheduled time.
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Minutes 10)
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings `
    -Description "Verified backup of the Coaching database" -Force | Out-Null
Write-Host "Scheduled task '$TaskName' registered: daily at $Time, keeping $Keep backups."
