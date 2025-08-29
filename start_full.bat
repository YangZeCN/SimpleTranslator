@echo off
chcp 65001 >nul
echo SimpleTranslator - Full Mode
echo Includes system tray and global hotkeys (may be unstable)
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found. Please install Python 3.13+
    pause
    exit /b 1
)

echo Starting SimpleTranslator (Full Mode)...
echo Note: If you encounter threading errors, please use Simple Mode instead
echo.
python main.py

if %errorlevel% neq 0 (
    echo.
    echo Error: Failed to start SimpleTranslator
    echo This might be a threading compatibility issue
    echo Try using Simple Mode: .\start_simple.bat
    echo Or install dependencies: pip install -r requirements.txt
    pause
)
