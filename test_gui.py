#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试GUI界面是否正常工作
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui import TranslatorGUI

def test_gui():
    """测试GUI创建"""
    try:
        print("创建GUI界面...")
        gui = TranslatorGUI()
        print("GUI创建成功！")
        
        # 显示窗口
        gui.show_window()
        print("界面显示成功！")
        
        # 运行事件循环（测试模式，5秒后自动关闭）
        gui.root.after(5000, gui.root.quit)  # 5秒后退出
        gui.root.mainloop()
        
        print("测试完成！")
        
    except Exception as e:
        print(f"GUI测试失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_gui()
