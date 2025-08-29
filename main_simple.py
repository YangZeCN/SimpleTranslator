#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SimpleTranslator 备用启动脚本
使用更简单的方式避免多线程问题
"""
import tkinter as tk
from tkinter import messagebox
import sys
import os
import time
import threading
from gui import TranslatorGUI
from config import Config

class SimpleTranslatorApp:
    def __init__(self):
        self.config = Config()
        self.gui = None
        self.running = True
        
    def create_simple_gui(self):
        """创建简单的主界面（无系统托盘）"""
        if self.gui is None:
            self.gui = TranslatorGUI(on_hide_callback=self.on_gui_hide)
        
        # 设置窗口关闭事件
        self.gui.root.protocol("WM_DELETE_WINDOW", self.minimize_to_background)
        
        # 显示界面
        self.gui.show_window()
        
        return self.gui
    
    def minimize_to_background(self):
        """最小化到后台"""
        if self.gui:
            self.gui.hide_window()
        print("程序已最小化，可以通过任务栏或重新运行程序来打开")
    
    def on_gui_hide(self):
        """GUI隐藏时的回调"""
        pass
    
    def show_gui(self):
        """显示GUI"""
        if self.gui is None:
            self.create_simple_gui()
        else:
            self.gui.show_window()
    
    def run(self):
        """运行应用（简单模式）"""
        print("SimpleTranslator 启动中（简单模式）...")
        print("注意：此模式没有系统托盘和全局热键功能")
        
        # 直接创建并显示GUI
        gui = self.create_simple_gui()
        
        print("SimpleTranslator 已启动！")
        print("关闭窗口会最小化程序，重新运行此脚本可以再次打开")
        
        try:
            # 运行GUI主循环
            gui.root.mainloop()
        except KeyboardInterrupt:
            print("接收到中断信号，正在退出...")
        except Exception as e:
            print(f"程序运行出错: {e}")
        finally:
            self.quit_app()
    
    def quit_app(self):
        """退出应用"""
        print("正在退出应用...")
        self.running = False
        
        if self.gui:
            try:
                self.gui.destroy()
            except:
                pass
        
        sys.exit(0)

def main():
    """主函数"""
    app = SimpleTranslatorApp()
    app.run()

if __name__ == "__main__":
    main()
