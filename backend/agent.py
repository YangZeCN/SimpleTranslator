from openai import OpenAI
from models import AgentConfig
from config import ModelConfig

class AgentApi:
    def __init__(self, agent_config: AgentConfig, model_config: ModelConfig):
        self.agent_config = agent_config
        self.model_config = model_config
        self.init_client()
    
    def init_client(self):
        """init client"""
        provider = self.agent_config.provider
        api_key = self.agent_config.api_key
        base_url = self.agent_config.base_url
        try:
            if provider == 'OpenAI':
                if api_key:
                    self.client = OpenAI(api_key=api_key)
                    return True
                    
            elif provider == 'DeepSeek':
                if api_key and base_url:
                    self.client = OpenAI(
                        api_key = api_key,
                        base_url = base_url
                    )
                    return True
                    
            elif provider == 'Custom':
                if api_key and base_url:
                    self.client = OpenAI(
                        api_key = api_key,
                        base_url=base_url
                    )
                    return True
                    
        except Exception as e:
            print(f"Init {provider} Client Failed: {e}")
            return False
        
        return False
    
    def _make_request(self, prompt):
        """发送API请求"""
        try:
            response = self.client.chat.completions.create(
                model=self.model_config.name,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=self.model_config.max_tokens,
                temperature=self.model_config.temperature,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"API请求失败: {str(e)}")
            raise Exception(f"API request failed: {str(e)}")
        
    
    def translate_text(self, text, target_lang="中文"):
        """翻译文本"""
        if target_lang.lower() in ['cn', '中文', 'zh']:
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
    
    def translate_text_with_mode(self, text, mode, target_lang="zh"):
        """根据不同模式处理文本"""
        if mode == 'translate':
            return self.translate_text(text, target_lang)
        elif mode == 'polish':
            return self.polish_english(text)
        elif mode == 'email':
            # 假设text包含邮件内容和中文信息，用特定分隔符分开
            try:
                email_content, chinese_info = text.split('|||')
                return self.write_email(email_content.strip(), chinese_info.strip())
            except ValueError:
                print("Error: For email mode, please provide both email content and Chinese info separated by '|||'.")
                raise ValueError("For email mode, please provide both email content and Chinese info separated by '|||'.")
        elif mode == 'chat':
            return self.chat_with_gpt(text)
        else:
            return "Error: Unsupported mode. Please choose from 'translate', 'polish', 'email', or 'chat'."
