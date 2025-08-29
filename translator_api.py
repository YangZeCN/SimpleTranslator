from openai import OpenAI
from config import Config

class TranslatorAPI:
    def __init__(self):
        self.config = Config()
        self.client = None
        self.current_provider = None
        self.init_client()
    
    def init_client(self):
        """初始化API客户端"""
        provider = self.config.get('api_provider', 'openai')
        self.current_provider = provider
        
        try:
            if provider == 'openai':
                api_key = self.config.get('openai_api_key')
                if api_key:
                    self.client = OpenAI(api_key=api_key)
                    return True
                    
            elif provider == 'deepseek':
                api_key = self.config.get('deepseek_api_key')
                if api_key:
                    self.client = OpenAI(
                        api_key=api_key,
                        base_url="https://api.deepseek.com"
                    )
                    return True
                    
            elif provider == 'custom':
                api_key = self.config.get('custom_api_key')
                base_url = self.config.get('custom_base_url')
                if api_key and base_url:
                    self.client = OpenAI(
                        api_key=api_key,
                        base_url=base_url
                    )
                    return True
                    
        except Exception as e:
            print(f"初始化{provider}客户端失败: {e}")
            return False
        
        return False
    
    def is_configured(self):
        """检查当前API是否已配置"""
        return self.client is not None and self.get_current_api_key()
    
    def get_current_api_key(self):
        """获取当前API提供商的密钥"""
        provider = self.config.get('api_provider', 'openai')
        if provider == 'openai':
            return self.config.get('openai_api_key')
        elif provider == 'deepseek':
            return self.config.get('deepseek_api_key')
        elif provider == 'custom':
            return self.config.get('custom_api_key')
        return None
    
    def get_current_model(self):
        """获取当前API提供商的模型"""
        provider = self.config.get('api_provider', 'openai')
        if provider == 'openai':
            return self.config.get('model', 'gpt-3.5-turbo')
        elif provider == 'deepseek':
            return self.config.get('deepseek_model', 'deepseek-chat')
        elif provider == 'custom':
            return self.config.get('custom_model', 'gpt-3.5-turbo')
        return 'gpt-3.5-turbo'
    
    def set_api_provider(self, provider):
        """设置API提供商"""
        self.config.set('api_provider', provider)
        return self.init_client()
    
    def set_api_key(self, api_key, provider=None):
        """设置API密钥"""
        if not provider:
            provider = self.config.get('api_provider', 'openai')
        
        if provider == 'openai':
            self.config.set('openai_api_key', api_key)
        elif provider == 'deepseek':
            self.config.set('deepseek_api_key', api_key)
        elif provider == 'custom':
            self.config.set('custom_api_key', api_key)
        
        return self.init_client()
    
    def set_custom_config(self, api_key, base_url, model):
        """设置自定义API配置"""
        self.config.set('custom_api_key', api_key)
        self.config.set('custom_base_url', base_url)
        self.config.set('custom_model', model)
        return self.init_client()
    
    def _make_request(self, prompt):
        """发送API请求"""
        if not self.is_configured():
            provider = self.config.get('api_provider', 'openai')
            return f"错误：请先配置{provider}的API密钥"
        
        try:
            model = self.get_current_model()
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=self.config.get('max_tokens'),
                temperature=self.config.get('temperature')
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"API请求失败: {str(e)}"
    
    def translate_text(self, text, target_lang="中文"):
        """翻译文本"""
        if target_lang.lower() in ['chinese', '中文', 'zh']:
            prompt = f"""请将以下文本翻译成中文，保持原意的准确性和流畅性：

{text}

请直接返回翻译结果，不要添加任何说明。"""
        else:
            prompt = f"""Please translate the following text to {target_lang}, maintaining accuracy and fluency:

{text}

Please return only the translation without any explanation."""
        
        return self._make_request(prompt)
    
    def polish_english(self, text):
        """英文润色，使其更像Native Speaker"""
        prompt = f"""Please polish the following English text to make it sound more natural and native-like. Improve grammar, word choice, and flow while maintaining the original meaning:

{text}

Please return only the polished text without any explanation."""
        
        return self._make_request(prompt)
    
    def write_email(self, email_content, chinese_info):
        """根据邮件内容和中文信息撰写邮件"""
        prompt = f"""Based on the following email content and additional Chinese information, please write a professional and appropriate email response:

Original Email Content:
{email_content}

Additional Information (in Chinese):
{chinese_info}

Please write a professional email response in English. Include appropriate greetings, body content, and closing."""
        
        return self._make_request(prompt)
    
    def chat_with_gpt(self, message):
        """与GPT自由对话"""
        return self._make_request(message)
