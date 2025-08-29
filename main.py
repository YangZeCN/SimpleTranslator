import tkinter as tk
from tkinter import messagebox
import pystray
from PIL import Image, ImageDraw
import threading
import keyboard
import sys
import os
import time
import signal
from gui import TranslatorGUI
from config import Config

class TranslatorApp:
    def __init__(self):
        self.config = Config()
        self.gui = None
        self.tray_icon = None
        self.running = True
        
    def create_tray_icon(self):
        """创建系统托盘图标"""
        # 创建一个简单的图标
        image = Image.new('RGB', (64, 64), color='blue')
        draw = ImageDraw.Draw(image)
        draw.text((10, 20), "T", fill='white', font_size=40)
        
        # 创建托盘菜单
        menu = pystray.Menu(
            pystray.MenuItem("打开翻译器", self.show_gui),
            pystray.MenuItem("设置", self.show_settings),
            pystray.MenuItem("退出", self.quit_app)
        )
        
        # 创建托盘图标
        self.tray_icon = pystray.Icon(
            "SimpleTranslator",
            image,
            "SimpleTranslator - 翻译小助手",
            menu
        )
        
    def setup_hotkey(self):
        """设置全局热键"""
        hotkey = self.config.get('hotkey', 'ctrl+shift+t')
        try:
            # 使用更安全的热键设置方式
            def hotkey_handler():
                try:
                    self.show_gui()
                except Exception as e:
                    print(f"热键处理失败: {e}")
            
            keyboard.add_hotkey(hotkey, hotkey_handler)
            print(f"热键 {hotkey} 已设置")
        except Exception as e:
            print(f"设置热键失败: {e}")
            print("程序将继续运行，但热键功能不可用")
    
    def show_gui(self):
        """显示GUI"""
        if self.gui is None:
            self.gui = TranslatorGUI(on_hide_callback=self.on_gui_hide)
        self.gui.show_window()
    
    def on_gui_hide(self):
        """GUI隐藏时的回调"""
        pass
    
    def show_settings(self):
        """显示设置窗口"""
        self.show_gui()  # 暂时直接显示主界面
    
    def quit_app(self):
        """退出应用"""
        print("正在退出应用...")
        self.running = False
        
        # 清理热键
        try:
            keyboard.unhook_all()
        except Exception as e:
            print(f"清理热键失败: {e}")
        
        # 关闭GUI
        if self.gui:
            try:
                self.gui.destroy()
            except Exception as e:
                print(f"关闭GUI失败: {e}")
        
        # 停止托盘图标
        if self.tray_icon:
            try:
                self.tray_icon.stop()
            except Exception as e:
                print(f"停止托盘图标失败: {e}")
        
        # 强制退出
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    
    def run(self):
        """运行应用"""
        print("SimpleTranslator 启动中...")
        
        # 创建系统托盘图标
        self.create_tray_icon()
        
        # 设置热键（在主线程中）
        self.setup_hotkey()
        
        print("SimpleTranslator 已启动，可通过系统托盘或热键使用")
        
        try:
            # 运行托盘图标（这会阻塞主线程）
            self.tray_icon.run()
        except KeyboardInterrupt:
            print("接收到中断信号，正在退出...")
            self.quit_app()
        except Exception as e:
            print(f"程序运行出错: {e}")
            self.quit_app()

def main():
    # 检查是否已有实例在运行
    app = TranslatorApp()
    app.run()

if __name__ == "__main__":
    main()
