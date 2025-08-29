@echo off
chcp 65001 >nul
echo SimpleTranslator - Simple Mode (Recommended)
echo Most stable mode with all core translation features
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found. Please install Python 3.13+
    pause
    exit /b 1
)

echo Starting SimpleTranslator (Simple Mode)...
echo.
python main_simple.py

if %errorlevel% neq 0 (
    echo.
    echo Error: Failed to start SimpleTranslator
    echo Please check if dependencies are installed:
    echo   pip install -r requirements.txt
    pause
)
