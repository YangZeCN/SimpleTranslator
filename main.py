#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SimpleTranslator - 最终托盘版本
如果双击不工作，提供替代方案
"""

import tkinter as tk
from tkinter import messagebox
import pystray
from PIL import Image, ImageDraw
import keyboard
import sys
import threading
import time
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

class TranslatorApp:
    def __init__(self):
        self.config = Config()
        self.gui = None
        self.tray_icon = None
        self.tray_thread = None
        self.running = True
        self._quitting = False
        self.click_count = 0
        self.last_click_time = 0
        
    def create_tray_icon(self):
        """创建系统托盘图标"""
        try:
            # 创建托盘图标
            image = Image.new('RGB', (64, 64), color=(70, 130, 180))
            draw = ImageDraw.Draw(image)
            draw.ellipse([16, 16, 48, 48], fill='white')
            draw.text((28, 24), "T", fill='black')
            
            # 创建菜单 - 让第一项更明显
            menu = pystray.Menu(
                pystray.MenuItem("🚀 点我打开翻译器", self.show_gui, default=True),
                pystray.MenuItem("⚙️ 设置", self.show_settings),
                pystray.MenuItem("❌ 退出程序", self.quit_app)
            )
            
            self.tray_icon = pystray.Icon(
                "SimpleTranslator",
                image,
                "SimpleTranslator - 右键点击打开菜单",
                menu
            )
            
            # 设置双击回调
            self.tray_icon.default_action = self.show_gui
            
            logging.info("托盘图标已创建")
            
        except Exception as e:
            logging.error(f"创建托盘图标失败: {e}")
            raise

    def setup_hotkey(self):
        """设置全局热键"""
        hotkey = self.config.get('hotkey', 'ctrl+shift+t')
        try:
            def hotkey_handler():
                logging.info("热键触发")
                self.show_gui()
            
            keyboard.add_hotkey(hotkey, hotkey_handler)
            logging.info(f"热键 {hotkey} 已设置")
            
        except Exception as e:
            logging.error(f"设置热键失败: {e}")

    def show_gui(self):
        """显示GUI界面 - 线程安全版本"""
        def _show_gui_safe():
            try:
                if not self.gui:
                    logging.info("创建新的GUI实例")
                    self.gui = TranslatorGUI(on_hide_callback=self.on_gui_hide)
                
                self.gui.show_window()
                logging.info("GUI显示完成")
                
            except Exception as e:
                logging.error(f"显示GUI失败: {e}")
        
        # 确保在主线程中执行GUI操作
        if self.gui and hasattr(self.gui, 'root'):
            self.gui.root.after(0, _show_gui_safe)
        else:
            # 如果GUI还不存在，直接在当前线程创建（启动时）
            _show_gui_safe()

    def on_gui_hide(self):
        """GUI隐藏时的回调"""
        logging.info("GUI隐藏")

    def show_settings(self):
        """显示设置窗口"""
        self.show_gui()

    def quit_app(self):
        """退出应用程序"""
        if self._quitting:
            return
        
        self._quitting = True
        logging.info("开始退出应用")
        
        self.running = False
        
        try:
            # 清理热键
            keyboard.unhook_all()
            logging.info("热键清理完成")
        except Exception as e:
            logging.error(f"清理热键失败: {e}")
        
        try:
            # 停止托盘图标
            if self.tray_icon:
                self.tray_icon.stop()
                logging.info("托盘图标停止完成")
        except Exception as e:
            logging.error(f"停止托盘图标失败: {e}")
        
        try:
            # 关闭GUI
            if self.gui:
                self.gui.root.after(0, self.gui.destroy)
                logging.info("GUI销毁完成")
        except Exception as e:
            logging.error(f"关闭GUI失败: {e}")
        
        # 等待托盘线程结束（避免在托盘线程中等待自己）
        if self.tray_thread and self.tray_thread.is_alive():
            # 检查是否在托盘线程中调用
            current_thread = threading.current_thread()
            if current_thread != self.tray_thread:
                self.tray_thread.join(timeout=2)
            else:
                # 如果在托盘线程中，只是标记退出
                logging.info("在托盘线程中退出，跳过join")
        
        logging.info("应用程序退出")

    def run_tray(self):
        """在单独线程中运行托盘"""
        try:
            logging.info("托盘线程启动")
            self.tray_icon.run()
        except Exception as e:
            logging.error(f"托盘运行失败: {e}")

    def run(self):
        """运行应用"""
        logging.info("SimpleTranslator 启动中...")
        
        try:
            # 1. 先创建GUI（主线程）
            logging.info("创建GUI...")
            self.gui = TranslatorGUI(on_hide_callback=self.on_gui_hide)
            self.gui.root.withdraw()  # 初始隐藏
            
            # 2. 设置热键
            logging.info("设置热键...")
            self.setup_hotkey()
            
            # 3. 创建托盘图标
            logging.info("创建托盘...")
            self.create_tray_icon()
            
            # 4. 在单独线程中启动托盘
            logging.info("启动托盘线程...")
            self.tray_thread = threading.Thread(target=self.run_tray, daemon=True)
            self.tray_thread.start()
            
            # 5. 设置窗口关闭处理 - 点击关闭按钮时隐藏窗口而不是退出
            self.gui.root.protocol("WM_DELETE_WINDOW", self.gui.hide_window)
            
            logging.info("SimpleTranslator 已启动，托盘图标应该可见")
            print("程序已启动！")
            print("")
            print("使用方法：")
            print("🔹 右键点击托盘图标 → 选择'🚀 点我打开翻译器'")
            print("🔹 尝试双击托盘图标（可能在某些系统上不工作）")
            print("🔹 使用热键：Ctrl+Shift+T")
            print("")
            print("如果双击不工作，这是已知的pystray兼容性问题，")
            print("请使用右键菜单或热键来打开翻译器。")
            
            # 6. 运行主GUI循环（阻塞）
            self.gui.root.mainloop()
            
        except Exception as e:
            logging.error(f"启动失败: {e}")
            messagebox.showerror("启动错误", f"程序启动失败: {e}")
        finally:
            self.quit_app()

def main():
    """主函数"""
    try:
        app = TranslatorApp()
        app.run()
    except KeyboardInterrupt:
        logging.info("用户中断程序")
    except Exception as e:
        logging.error(f"程序运行失败: {e}")
        messagebox.showerror("运行错误", f"程序运行失败: {e}")
    finally:
        sys.exit(0)

if __name__ == "__main__":
    main()
