@echo off
chcp 65001 >nul
echo SimpleTranslator Launcher
echo.

REM Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found. Please install Python 3.13+
    pause
    exit /b 1
)

echo Using Python: 
python --version

REM Check dependencies
echo Checking dependencies...
python -c "import openai, tkinter, pyperclip; print('Core dependencies OK')" 2>nul
if %errorlevel% neq 0 (
    echo Dependencies not fully installed. Installing...
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Failed to install dependencies. Please check network connection.
        pause
        exit /b 1
    )
)

echo.
echo Choose startup mode:
echo 1. Simple Mode (Recommended - Most Stable)
echo 2. Full Mode (System tray + Hotkeys)
echo.
set /p choice="Choose mode (1/2, default 1): "

if "%choice%"=="2" (
    echo Starting Full Mode...
    echo Note: If you encounter threading errors, please use Simple Mode
    python main.py
) else (
    echo Starting Simple Mode...
    python main_simple.py
)

pause
