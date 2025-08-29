#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SimpleTranslator - 仅热键版本
避免系统托盘相关的 GIL 和线程问题
只使用全局热键 Ctrl+Shift+T 来启动翻译界面
"""

import tkinter as tk
from tkinter import messagebox
import keyboard
import sys
import logging
from gui import TranslatorGUI
from config import Config

# 设置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("translator.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)

class SimpleTranslatorApp:
    def __init__(self):
        self.config = Config()
        self.gui = None
        self.running = True
        
    def setup_hotkey(self):
        """设置全局热键"""
        hotkey = self.config.get('hotkey', 'ctrl+shift+t')
        try:
            def hotkey_handler():
                logging.info("热键触发")
                try:
                    if not self.gui:
                        self.gui = TranslatorGUI(on_hide_callback=self.on_gui_hide)
                    self.gui.show_window()
                except Exception as e:
                    logging.error(f"显示GUI失败: {e}")
                    messagebox.showerror("错误", f"显示翻译界面失败: {e}")
            
            keyboard.add_hotkey(hotkey, hotkey_handler)
            logging.info(f"热键 {hotkey} 已设置")
            print(f"热键设置成功！按 {hotkey} 打开翻译器")
            
        except Exception as e:
            logging.error(f"设置热键失败: {e}")
            messagebox.showerror("错误", f"设置热键失败: {e}")
    
    def on_gui_hide(self):
        """GUI隐藏时的回调"""
        logging.info("GUI隐藏")
    
    def run(self):
        """运行应用"""
        logging.info("SimpleTranslator 启动中（仅热键模式）...")
        print("SimpleTranslator 仅热键模式启动")
        print("按 Ctrl+Shift+T 打开翻译器")
        print("按 Ctrl+C 退出程序")
        
        # 设置热键
        self.setup_hotkey()
        
        logging.info("SimpleTranslator 已启动（仅热键模式）")
        
        try:
            # 保持程序运行，等待热键触发
            keyboard.wait()  # 这会阻塞，直到程序被终止
        except KeyboardInterrupt:
            logging.info("用户中断程序")
            self.quit_app()
        except Exception as e:
            logging.error(f"程序运行错误: {e}")
            self.quit_app()
    
    def quit_app(self):
        """退出应用"""
        logging.info("退出应用")
        self.running = False
        
        try:
            keyboard.unhook_all()
            logging.info("热键清理完成")
        except Exception as e:
            logging.error(f"清理热键失败: {e}")
        
        if self.gui:
            try:
                self.gui.destroy()
                logging.info("GUI销毁完成")
            except Exception as e:
                logging.error(f"关闭GUI失败: {e}")
        
        logging.info("应用程序退出")
        sys.exit(0)

def main():
    """主函数"""
    try:
        app = SimpleTranslatorApp()
        app.run()
    except Exception as e:
        logging.error(f"程序启动失败: {e}")
        messagebox.showerror("启动错误", f"程序启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
