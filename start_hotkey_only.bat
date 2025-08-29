@echo off
echo 启动 SimpleTranslator (仅热键模式)
echo 这个版本不使用系统托盘，避免线程和GIL问题
echo 按 Ctrl+Shift+T 打开翻译器
echo 按 Ctrl+C 退出程序
echo.
python main_hotkey_only.py
pause
