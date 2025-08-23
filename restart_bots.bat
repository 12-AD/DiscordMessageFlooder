@echo off
REM Restart all bots safely

echo Stopping bots...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0stop_bots.ps1"

REM Wait a couple of seconds to ensure all processes are fully stopped
timeout /t 2 /nobreak >nul

echo Starting bots...
cscript //nologo "%~dp0start_bots.vbs"

echo Bots restarted!

