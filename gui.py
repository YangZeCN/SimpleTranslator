import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import pyperclip
import threading
from translator_api import TranslatorAPI

class TranslatorGUI:
    def __init__(self, on_hide_callback=None):
        self.on_hide_callback = on_hide_callback
        self.api = TranslatorAPI()
        self.setup_ui()
        
    def setup_ui(self):
        self.root = tk.Tk()
        self.root.title("SimpleTranslator - 翻译小助手")
        self.root.geometry("700x600")
        self.root.configure(bg='#f0f0f0')
        
        # 设置窗口关闭事件
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)
        
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # API配置区域
        config_frame = ttk.LabelFrame(main_frame, text="API配置", padding="5")
        config_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        config_frame.columnconfigure(1, weight=1)
        
        # API提供商选择
        ttk.Label(config_frame, text="API提供商:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.api_provider_var = tk.StringVar(value=self.api.config.get('api_provider', 'openai'))
        provider_combo = ttk.Combobox(config_frame, textvariable=self.api_provider_var, 
                                    values=["openai", "deepseek", "custom"], state="readonly", width=15)
        provider_combo.grid(row=0, column=1, sticky=tk.W, padx=(0, 5))
        provider_combo.bind('<<ComboboxSelected>>', self.on_provider_change)
        
        # API密钥配置
        ttk.Label(config_frame, text="API Key:").grid(row=1, column=0, sticky=tk.W, padx=(0, 5))
        self.api_key_var = tk.StringVar()
        self.api_key_entry = ttk.Entry(config_frame, textvariable=self.api_key_var, show="*", width=50)
        self.api_key_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        
        # 自定义API配置框架（初始隐藏）
        self.custom_frame = ttk.Frame(config_frame)
        ttk.Label(self.custom_frame, text="Base URL:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.custom_base_url_var = tk.StringVar(value=self.api.config.get('custom_base_url', ''))
        ttk.Entry(self.custom_frame, textvariable=self.custom_base_url_var, width=40).grid(row=0, column=1, sticky=(tk.W, tk.E))
        
        ttk.Label(self.custom_frame, text="Model:").grid(row=1, column=0, sticky=tk.W, padx=(0, 5))
        self.custom_model_var = tk.StringVar(value=self.api.config.get('custom_model', 'gpt-3.5-turbo'))
        ttk.Entry(self.custom_frame, textvariable=self.custom_model_var, width=30).grid(row=1, column=1, sticky=tk.W)
        self.custom_frame.columnconfigure(1, weight=1)
        
        # 保存按钮
        ttk.Button(config_frame, text="保存配置", command=self.save_api_config).grid(row=3, column=1, sticky=tk.E, pady=(5, 0))
        
        # 初始化API密钥显示
        self.update_api_key_display()
        
        # 功能模式选择
        mode_frame = ttk.LabelFrame(main_frame, text="功能模式", padding="5")
        mode_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.mode_var = tk.StringVar(value="translate")
        modes = [
            ("翻译", "translate"),
            ("英文润色", "polish"),
            ("邮件撰写", "email"),
            ("自由对话", "chat")
        ]
        
        for i, (text, value) in enumerate(modes):
            ttk.Radiobutton(mode_frame, text=text, variable=self.mode_var, 
                          value=value, command=self.on_mode_change).grid(row=0, column=i, padx=10)
        
        # 输入区域
        input_frame = ttk.LabelFrame(main_frame, text="输入", padding="5")
        input_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        input_frame.columnconfigure(0, weight=1)
        input_frame.rowconfigure(0, weight=1)
        
        self.input_text = scrolledtext.ScrolledText(input_frame, height=8, wrap=tk.WORD)
        self.input_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 5))
        
        # 特殊输入框（用于邮件撰写模式）
        self.email_info_frame = ttk.Frame(input_frame)
        ttk.Label(self.email_info_frame, text="附加信息（中文）:").grid(row=0, column=0, sticky=tk.W)
        self.email_info_text = scrolledtext.ScrolledText(self.email_info_frame, height=3, wrap=tk.WORD)
        self.email_info_text.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(5, 0))
        self.email_info_frame.columnconfigure(0, weight=1)
        
        # 翻译目标语言选择（翻译模式）
        self.translate_frame = ttk.Frame(input_frame)
        ttk.Label(self.translate_frame, text="目标语言:").grid(row=0, column=0, sticky=tk.W)
        self.target_lang_var = tk.StringVar(value="中文")
        lang_combo = ttk.Combobox(self.translate_frame, textvariable=self.target_lang_var, 
                                values=["中文", "English", "日本語", "Français", "Deutsch"], state="readonly")
        lang_combo.grid(row=0, column=1, padx=(5, 0))
        
        # 按钮区域
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=2, column=0, pady=(5, 0))
        
        ttk.Button(button_frame, text="粘贴", command=self.paste_text).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(button_frame, text="清空", command=self.clear_input).grid(row=0, column=1, padx=(0, 5))
        ttk.Button(button_frame, text="处理", command=self.process_text).grid(row=0, column=2, padx=(0, 5))
        
        # 输出区域
        output_frame = ttk.LabelFrame(main_frame, text="输出", padding="5")
        output_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=8, wrap=tk.WORD, state=tk.DISABLED)
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 5))
        
        # 输出按钮
        output_button_frame = ttk.Frame(output_frame)
        output_button_frame.grid(row=1, column=0)
        
        ttk.Button(output_button_frame, text="复制结果", command=self.copy_result).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(output_button_frame, text="清空输出", command=self.clear_output).grid(row=0, column=1)
        
        # 配置行列权重
        main_frame.rowconfigure(2, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # 初始化界面
        self.on_mode_change()
        self.update_custom_frame_visibility()
        
    def on_mode_change(self):
        """模式切换时更新界面"""
        mode = self.mode_var.get()
        
        # 隐藏所有特殊框架
        self.email_info_frame.grid_remove()
        self.translate_frame.grid_remove()
        
        # 根据模式显示相应的控件
        if mode == "email":
            self.email_info_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(5, 0))
        elif mode == "translate":
            self.translate_frame.grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
    
    def on_provider_change(self, event=None):
        """API提供商切换时的处理"""
        self.update_api_key_display()
        self.update_custom_frame_visibility()
    
    def update_api_key_display(self):
        """更新API密钥显示"""
        provider = self.api_provider_var.get()
        if provider == 'openai':
            key = self.api.config.get('openai_api_key', '')
        elif provider == 'deepseek':
            key = self.api.config.get('deepseek_api_key', '')
        elif provider == 'custom':
            key = self.api.config.get('custom_api_key', '')
        else:
            key = ''
        self.api_key_var.set(key)
    
    def update_custom_frame_visibility(self):
        """更新自定义API配置框架的可见性"""
        provider = self.api_provider_var.get()
        if provider == 'custom':
            self.custom_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(5, 0))
        else:
            self.custom_frame.grid_remove()
    
    def save_api_config(self):
        """保存API配置"""
        provider = self.api_provider_var.get()
        api_key = self.api_key_var.get().strip()
        
        if not api_key:
            messagebox.showwarning("警告", "请输入API密钥")
            return
        
        # 设置API提供商
        self.api.set_api_provider(provider)
        
        success = False
        if provider == 'custom':
            base_url = self.custom_base_url_var.get().strip()
            model = self.custom_model_var.get().strip()
            if not base_url:
                messagebox.showwarning("警告", "请输入Base URL")
                return
            if not model:
                messagebox.showwarning("警告", "请输入Model名称")
                return
            success = self.api.set_custom_config(api_key, base_url, model)
        else:
            success = self.api.set_api_key(api_key, provider)
        
        if success:
            provider_names = {
                'openai': 'OpenAI',
                'deepseek': 'DeepSeek',
                'custom': '自定义API'
            }
            messagebox.showinfo("成功", f"{provider_names.get(provider, provider)}配置保存成功！")
        else:
            messagebox.showerror("错误", "API配置无效或网络连接失败")
    
    def paste_text(self):
        """粘贴剪贴板内容"""
        try:
            clipboard_text = pyperclip.paste()
            self.input_text.delete(1.0, tk.END)
            self.input_text.insert(1.0, clipboard_text)
        except Exception as e:
            messagebox.showerror("错误", f"粘贴失败: {str(e)}")
    
    def clear_input(self):
        """清空输入"""
        self.input_text.delete(1.0, tk.END)
        if hasattr(self, 'email_info_text'):
            self.email_info_text.delete(1.0, tk.END)
    
    def clear_output(self):
        """清空输出"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)
    
    def copy_result(self):
        """复制结果到剪贴板"""
        try:
            result = self.output_text.get(1.0, tk.END).strip()
            if result:
                pyperclip.copy(result)
                messagebox.showinfo("成功", "结果已复制到剪贴板")
            else:
                messagebox.showwarning("警告", "没有可复制的内容")
        except Exception as e:
            messagebox.showerror("错误", f"复制失败: {str(e)}")
    
    def process_text(self):
        """处理文本"""
        input_text = self.input_text.get(1.0, tk.END).strip()
        if not input_text:
            messagebox.showwarning("警告", "请输入要处理的文本")
            return
        
        if not self.api.is_configured():
            messagebox.showerror("错误", "请先配置OpenAI API密钥")
            return
        
        # 在新线程中处理，避免界面卡顿
        threading.Thread(target=self._process_text_thread, args=(input_text,), daemon=True).start()
    
    def _process_text_thread(self, input_text):
        """在后台线程中处理文本"""
        mode = self.mode_var.get()
        
        try:
            # 显示处理中状态
            self.root.after(0, lambda: self.show_output("处理中，请稍候..."))
            
            result = ""
            if mode == "translate":
                target_lang = self.target_lang_var.get()
                result = self.api.translate_text(input_text, target_lang)
            elif mode == "polish":
                result = self.api.polish_english(input_text)
            elif mode == "email":
                email_info = self.email_info_text.get(1.0, tk.END).strip()
                result = self.api.write_email(input_text, email_info)
            elif mode == "chat":
                result = self.api.chat_with_gpt(input_text)
            
            # 在主线程中更新界面
            self.root.after(0, lambda: self.show_output(result))
            
        except Exception as e:
            self.root.after(0, lambda: self.show_output(f"处理失败: {str(e)}"))
    
    def show_output(self, text):
        """显示输出结果"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, text)
        self.output_text.config(state=tk.DISABLED)
    
    def show_window(self):
        """显示窗口"""
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
    
    def hide_window(self):
        """隐藏窗口"""
        self.root.withdraw()
        if self.on_hide_callback:
            self.on_hide_callback()
    
    def destroy(self):
        """销毁窗口"""
        try:
            self.root.quit()  # 停止事件循环
            self.root.destroy()
        except Exception as e:
            import logging
            logging.error(f"销毁窗口失败: {e}")
