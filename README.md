# SimpleTranslator - 翻译小助手

一个基于Python + ChatGPT API的本地翻译助手，支持多种翻译和文本处理功能。

## 功能特性

### 基本功能
- **多API支持**: 支持OpenAI、DeepSeek、自定义API等多种AI服务
- **文本翻译**: 支持多语言互译（中文、英文、日文、法文、德文等）
- **英文润色**: 将英文文本优化为更自然的Native Speaker表达
- **邮件撰写**: 根据原邮件内容和中文补充信息自动撰写专业邮件回复
- **自由对话**: 与ChatGPT进行自由对话交流

### API服务商支持
- **OpenAI**: 技术最成熟，英文处理最佳
- **DeepSeek**: 价格便宜，中文支持优秀，国内访问稳定
- **自定义API**: 支持其他兼容OpenAI格式的AI服务

### 便捷特性
- **后台运行**: 程序以exe形式在后台运行，占用资源少
- **系统托盘**: 最小化到系统托盘，右键菜单快速访问
- **全局热键**: 默认Ctrl+Shift+T快速唤出界面
- **一键复制**: 自动复制处理结果到剪贴板
- **配置保存**: 自动保存多个API密钥和用户偏好设置

## 安装和使用

### 方法1: 直接运行Python脚本

1. **安装依赖**:
   ```bash
   pip install -r requirements.txt
   ```

2. **配置API密钥**:
   - 运行程序后在界面中选择API提供商（OpenAI/DeepSeek/自定义）
   - 输入对应的API密钥
   - 或直接编辑`config.json`文件

3. **运行程序**:
   ```bash
   python main.py
   ```

### 方法2: 构建exe文件

1. **使用构建脚本**:
   ```bash
   python build.py
   ```
   选择选项3进行完整构建

2. **运行exe**:
   - 生成的`SimpleTranslator.exe`位于`dist`目录
   - 双击运行，程序将在后台启动
   - 通过系统托盘图标或热键Ctrl+Shift+T使用

## 使用说明

### 初次设置
1. 获取API密钥：
   - **OpenAI**: 访问 https://platform.openai.com/api-keys
   - **DeepSeek**: 访问 https://platform.deepseek.com/ （推荐国内用户）
   - **其他**: 使用自定义API配置
2. 在程序界面的"API配置"区域选择提供商并输入密钥

### 功能使用

#### 翻译功能
1. 选择"翻译"模式
2. 选择目标语言
3. 输入要翻译的文本
4. 点击"处理"获得翻译结果

#### 英文润色
1. 选择"英文润色"模式
2. 输入需要优化的英文文本
3. 点击"处理"获得润色后的文本

#### 邮件撰写
1. 选择"邮件撰写"模式
2. 在主输入框粘贴原邮件内容
3. 在"附加信息"框输入中文补充说明
4. 点击"处理"生成邮件回复

#### 自由对话
1. 选择"自由对话"模式
2. 输入想要询问的问题
3. 点击"处理"获得ChatGPT回复

### 快捷操作
- **粘贴**: 快速粘贴剪贴板内容到输入框
- **复制结果**: 将处理结果复制到剪贴板
- **全局热键**: Ctrl+Shift+T随时唤出程序界面

## 配置选项

程序支持以下配置（在`config.json`中）：

```json
{
  "api_provider": "deepseek",
  "openai_api_key": "your-openai-key-here",
  "deepseek_api_key": "your-deepseek-key-here",
  "custom_api_key": "your-custom-key-here",
  "custom_base_url": "https://your-api-url.com",
  "model": "gpt-3.5-turbo",
  "deepseek_model": "deepseek-chat",
  "custom_model": "your-model-name",
  "max_tokens": 1000,
  "temperature": 0.7,
  "hotkey": "ctrl+shift+t",
  "window_size": "700x600",
  "always_on_top": false,
  "auto_copy_result": true
}
```

## 系统要求

- Windows 10/11
- Python 3.8+
- 有效的OpenAI API密钥
- 网络连接

## 注意事项

1. **API费用**: 
   - OpenAI费用相对较高，但技术最成熟
   - DeepSeek价格便宜，中文支持优秀
   - 请根据需求选择合适的服务商
2. **网络连接**: 程序需要网络连接才能调用API
3. **API限制**: 遵守各服务商的使用条款和频率限制
4. **隐私保护**: 输入的文本会发送到对应的AI服务器进行处理

## 技术架构

- **GUI框架**: Tkinter
- **API客户端**: OpenAI Python库
- **系统托盘**: pystray
- **全局热键**: keyboard
- **剪贴板**: pyperclip
- **打包工具**: PyInstaller

## 开发者

项目地址: https://github.com/YangZeCN/SimpleTranslator

## 许可证

MIT License
