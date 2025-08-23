# Folder containing your bots
$botFolder = "$PSScriptRoot\bots"

# Get all python processes
Get-CimInstance Win32_Process | Where-Object {
    ($_.Name -eq "python.exe" -or $_.Name -eq "pythonw.exe") -and ($_.CommandLine -like "*$botFolder*")
} | ForEach-Object {
    Write-Host "Killing process $($_.ProcessId) running $($_.CommandLine)"
    Stop-Process -Id $_.ProcessId -Force
}
