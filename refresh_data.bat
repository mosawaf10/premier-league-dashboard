
@echo off
cd /d "%~dp0"

python scraper.py
if errorlevel 1 goto error

python top_scorers_scraper.py
if errorlevel 1 goto error

echo Data refreshed successfully!
pause
exit /b 0

:error
echo Data refresh failed.
pause
