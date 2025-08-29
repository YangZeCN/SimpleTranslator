import json
import os

class Config:
    def __init__(self):
        self.config_file = "config.json"
        self.default_config = {
            "api_provider": "openai",
            "openai_api_key": "",
            "deepseek_api_key": "",
            "custom_api_key": "",
            "custom_base_url": "",
            "model": "gpt-3.5-turbo",
            "deepseek_model": "deepseek-chat",
            "custom_model": "gpt-3.5-turbo",
            "max_tokens": 1000,
            "temperature": 0.7,
            "hotkey": "ctrl+shift+t",
            "window_size": "700x600",
            "always_on_top": False,
            "auto_copy_result": True
        }
        self.config = self.load_config()
    
    def load_config(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    # 合并默认配置，确保所有键都存在
                    for key, value in self.default_config.items():
                        if key not in config:
                            config[key] = value
                    return config
            except:
                return self.default_config.copy()
        return self.default_config.copy()
    
    def save_config(self):
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def get(self, key, default=None):
        """获取配置值，支持默认值"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        self.save_config()
