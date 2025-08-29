@echo off
echo SimpleTranslator 启动脚本
echo.

REM 优先使用Python 3.13，如果没有则使用默认python
py -3.13 --version >nul 2>&1
if %errorlevel% == 0 (
    set PYTHON_CMD=py -3.13
    echo 使用 Python 3.13
) else (
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo 错误: 未找到Python，请先安装Python
        pause
        exit /b 1
    )
    set PYTHON_CMD=python
    echo 使用默认 Python
)

REM 检查是否已安装依赖
echo 检查依赖包...
%PYTHON_CMD% -c "import openai, pystray, PIL, keyboard, pyperclip" 2>nul
if %errorlevel% neq 0 (
    echo 依赖包未完全安装，正在安装...
    %PYTHON_CMD% -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo 依赖安装失败，请检查网络连接
        pause
        exit /b 1
    )
)

echo 启动SimpleTranslator...
%PYTHON_CMD% main.py

pause
