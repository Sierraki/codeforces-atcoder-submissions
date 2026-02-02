@echo off
REM Harwest Control Panel - The one batch to rule them all!
title Harwest Control Panel
chcp 65001 >nul
setlocal enabledelayedexpansion
color 0A
REM Modern Harwest Automation Menu
REM (rest of the menu code goes here, copy from previous harwest_menu.bat minus the rename message)

:main_menu
cls
echo.
echo =============================================
echo      Harwest Automation Menu (2026 Edition)
echo =============================================
echo.
echo  [1] Harvest Codeforces
echo  [2] Harvest AtCoder
echo  [3] Harvest Both Platforms
echo  [4] System Reset and Update User Info
echo  [5] Download Requirements
echo  [6] View Last Update Status
echo  [7] Help
echo  [0] Exit
echo.
set /p main_choice=Select an option (0-7): 

if "%main_choice%"=="1" goto scan_mode_cf
if "%main_choice%"=="2" goto scan_mode_ac
if "%main_choice%"=="3" goto scan_mode_both
if "%main_choice%"=="4" goto full_reset
if "%main_choice%"=="5" goto download_requirements
if "%main_choice%"=="6" goto view_status
if "%main_choice%"=="7" goto help
if "%main_choice%"=="0" goto end
color 0C
echo Invalid choice. Please enter a number from 0 to 7.
color 0A
timeout /t 2 >nul
goto main_menu

:scan_mode_cf
cls
echo.
echo Codeforces: Select scan mode:
echo  [1] Normal scan
echo  [2] Full scan (all history)
echo  [0] Back to main menu
set /p scan_choice=Enter choice (0-2): 
if "%scan_choice%"=="1" (
    color 0E
    echo.
    echo Running: python -m harwest codeforces
    color 0A
    python -m harwest codeforces
    color 0A
    goto pause_and_return
) else (
    if "%scan_choice%"=="2" (
        color 0E
        echo.
        echo Running: python -m harwest codeforces --full-scan
        color 0A
        python -m harwest codeforces --full-scan
        color 0A
        goto pause_and_return
    ) else (
        if "%scan_choice%"=="0" (
            goto main_menu
        ) else (
            color 0C
            echo Invalid scan mode.
            color 0A
            timeout /t 2 >nul
            goto scan_mode_cf
        )
    )
)

:scan_mode_ac
cls
echo.
echo AtCoder: Select scan mode:
echo  [1] Normal scan
echo  [2] Full scan (all history)
echo  [0] Back to main menu
set /p scan_choice=Enter choice (0-2): 
if "%scan_choice%"=="1" (
    color 0E
    echo.
    echo Running: python -m harwest atcoder
    color 0A
    python -m harwest atcoder
    color 0A
    goto pause_and_return
) else (
    if "%scan_choice%"=="2" (
        color 0E
        echo.
        echo Running: python -m harwest atcoder --full-scan
        color 0A
        python -m harwest atcoder --full-scan
        color 0A
        goto pause_and_return
    ) else (
        if "%scan_choice%"=="0" (
            goto main_menu
        ) else (
            color 0C
            echo Invalid scan mode.
            color 0A
            timeout /t 2 >nul
            goto scan_mode_ac
        )
    )
)

:scan_mode_both
cls
echo.
echo Both platforms: Select scan mode:
echo  [1] Normal scan
echo  [2] Full scan (all history)
echo  [0] Back to main menu
set /p scan_choice=Enter choice (0-2): 
if "%scan_choice%"=="1" (
    color 0E
    echo.
    echo Running: python -m harwest codeforces
    color 0A
    python -m harwest codeforces
    color 0E
    echo Running: python -m harwest atcoder
    color 0A
    python -m harwest atcoder
    color 0A
    goto pause_and_return
) else (
    if "%scan_choice%"=="2" (
        color 0E
        echo.
        echo Running: python -m harwest codeforces --full-scan
        color 0A
        python -m harwest codeforces --full-scan
        color 0E
        echo Running: python -m harwest atcoder --full-scan
        color 0A
        python -m harwest atcoder --full-scan
        color 0A
        goto pause_and_return
    ) else (
        if "%scan_choice%"=="0" (
            goto main_menu
        ) else (
            color 0C
            echo Invalid scan mode.
            color 0A
            timeout /t 2 >nul
            goto scan_mode_both
        )
    )
)

:full_reset
cls
color 0E
echo.
echo Running system reset and update user info (fresh_start.py)...
color 0A
python fresh_start.py
color 0A
goto pause_and_return

:download_requirements
cls
color 0E
echo.
echo Installing Python requirements...
color 0A
pip install -r requirements.txt
color 0A
goto pause_and_return

:view_status
cls
color 0E
echo.
echo Last Update Status:
color 0A
python -c "import json,os; f='submissions/.harwest_timestamps.json'; d=json.load(open(f)) if os.path.exists(f) else {}; print(json.dumps(d, indent=2))" 2>nul || echo "No status file found. Run a harvest first."
color 0A
goto pause_and_return

:help
cls
echo.
echo ================= Help =================
echo 1. Harvest Codeforces: Fetches new Codeforces submissions.
echo 2. Harvest AtCoder: Fetches new AtCoder submissions.
echo 3. Harvest Both: Runs both harvesters in sequence.
echo 4. System Reset and Update User Info: Clears all data and reconfigures setup.
echo 5. Download Requirements: Installs required Python packages from requirements.txt
echo 6. View Last Update Status: Shows when submissions were last updated and how many new submissions were found.
echo 7. Help: Shows this help message.
echo 0. Exit: Close this menu.
echo.
echo === SMART SCHEDULE FEATURE ===
echo Timestamps are ONLY updated when new submissions are found.
echo This helps with intelligent scheduling - your task scheduler can check
echo the timestamp to skip runs when there are no new submissions!
echo.
pause
goto main_menu

:pause_and_return
echo.
echo Press any key to return to the main menu...
pause >nul
goto main_menu

:end
cls
color 07
echo.
echo Thank you for using Harwest Automation!
echo Goodbye!
timeout /t 2 >nul
exit /b
