import tkinter as tk
from tkinter import messagebox
import pystray
from PIL import Image, ImageDraw
import threading
import keyboard
import sys
import os
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
        hotkey = self.config.get('hotkey')
        try:
            keyboard.add_hotkey(hotkey, self.show_gui)
            print(f"热键 {hotkey} 已设置")
        except Exception as e:
            print(f"设置热键失败: {e}")
    
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
        self.running = False
        if self.gui:
            self.gui.destroy()
        if self.tray_icon:
            self.tray_icon.stop()
        sys.exit(0)
    
    def run(self):
        """运行应用"""
        print("SimpleTranslator 启动中...")
        
        # 创建系统托盘图标
        self.create_tray_icon()
        
        # 设置热键
        self.setup_hotkey()
        
        # 在单独线程中运行托盘图标
        tray_thread = threading.Thread(target=self.tray_icon.run, daemon=True)
        tray_thread.start()
        
        print("SimpleTranslator 已启动，可通过系统托盘或热键使用")
        
        try:
            # 保持主线程运行
            while self.running:
                threading.Event().wait(1)
        except KeyboardInterrupt:
            self.quit_app()

def main():
    # 检查是否已有实例在运行
    app = TranslatorApp()
    app.run()

if __name__ == "__main__":
    main()
