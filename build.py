import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox

def create_exe():
    """使用PyInstaller创建exe文件"""
    try:
        # 检查PyInstaller是否安装
        subprocess.run([sys.executable, "-c", "import PyInstaller"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("PyInstaller未安装，正在安装...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # PyInstaller命令
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",  # 单文件模式
        "--windowed",  # 无控制台窗口
        "--name", "SimpleTranslator",
        "--add-data", "config.json;.",  # 包含配置文件
        "--hidden-import", "PIL._tkinter_finder",
        "main.py"
    ]
    
    print("正在创建exe文件...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("exe文件创建成功！")
        print("文件位置: dist/SimpleTranslator.exe")
        return True
    else:
        print("创建exe文件失败:")
        print(result.stderr)
        return False

def install_dependencies():
    """安装依赖包"""
    print("正在安装依赖包...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("依赖包安装成功！")
        return True
    except subprocess.CalledProcessError as e:
        print(f"依赖包安装失败: {e}")
        return False

def main():
    print("SimpleTranslator 构建工具")
    print("1. 安装依赖包")
    print("2. 创建exe文件")
    print("3. 完整构建（安装依赖 + 创建exe）")
    
    choice = input("请选择操作 (1/2/3): ").strip()
    
    if choice == "1":
        install_dependencies()
    elif choice == "2":
        create_exe()
    elif choice == "3":
        if install_dependencies():
            create_exe()
    else:
        print("无效选择")

if __name__ == "__main__":
    main()
