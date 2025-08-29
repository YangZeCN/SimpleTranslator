# SimpleTranslator PowerShell 启动脚本
Write-Host "SimpleTranslator 启动脚本" -ForegroundColor Green
Write-Host ""

# 检测Python版本并选择最佳的
$pythonCmd = $null

# 优先尝试Python 3.13
try {
    $null = & py -3.13 --version 2>$null
    if ($LASTEXITCODE -eq 0) {
        $pythonCmd = "py -3.13"
        Write-Host "使用 Python 3.13" -ForegroundColor Yellow
    }
} catch {
    # Python 3.13不可用
}

# 如果没有3.13，尝试通用的py命令
if (-not $pythonCmd) {
    try {
        $null = & py --version 2>$null
        if ($LASTEXITCODE -eq 0) {
            $pythonCmd = "py"
            Write-Host "使用 Python Launcher" -ForegroundColor Yellow
        }
    } catch {
        # py命令不可用
    }
}

# 最后尝试python命令
if (-not $pythonCmd) {
    try {
        $null = & python --version 2>$null
        if ($LASTEXITCODE -eq 0) {
            $pythonCmd = "python"
            Write-Host "使用默认 Python" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "错误: 未找到Python，请先安装Python" -ForegroundColor Red
        Read-Host "按任意键退出"
        exit 1
    }
}

if (-not $pythonCmd) {
    Write-Host "错误: 无法找到可用的Python解释器" -ForegroundColor Red
    Read-Host "按任意键退出"
    exit 1
}

# 检查依赖包
Write-Host "检查依赖包..." -ForegroundColor Blue
try {
    $checkResult = & $pythonCmd.Split() -c "import openai, pystray, PIL, keyboard, pyperclip; print('OK')" 2>$null
    if ($LASTEXITCODE -ne 0 -or $checkResult -notcontains "OK") {
        Write-Host "依赖包未完全安装，正在安装..." -ForegroundColor Yellow
        & $pythonCmd.Split() -m pip install -r requirements.txt
        if ($LASTEXITCODE -ne 0) {
            Write-Host "依赖安装失败，请检查网络连接" -ForegroundColor Red
            Read-Host "按任意键退出"
            exit 1
        }
    } else {
        Write-Host "依赖包检查通过" -ForegroundColor Green
    }
} catch {
    Write-Host "依赖包检查失败，正在尝试安装..." -ForegroundColor Yellow
    & $pythonCmd.Split() -m pip install -r requirements.txt
}

# 启动程序
Write-Host "启动SimpleTranslator..." -ForegroundColor Green
Write-Host "程序将在后台运行，可通过系统托盘或快捷键 Ctrl+Shift+T 使用" -ForegroundColor Cyan
Write-Host "关闭此窗口不会停止程序运行" -ForegroundColor Cyan
Write-Host ""

try {
    & $pythonCmd.Split() main.py
} catch {
    Write-Host "程序启动失败: $_" -ForegroundColor Red
    Read-Host "按任意键退出"
}
