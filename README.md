# SimpleTranslator - AI翻译小助手

> **🤖 AI Generated Project | AI自动生成项目**  
> 本项目**完全由AI自动生成**，基于 **GitHub Copilot + Claude 4 Sonnet** 模型开发！  
> *This project is **100% AI-generated** using **GitHub Copilot + Claude 4 Sonnet**!*

一个基于Python + AI API的本地翻译助手，支持多种翻译和文本处理功能。

## ✨ 功能特性

> **🌟 AI开发亮点**: 本项目展示了AI在复杂软件开发中的能力，包括GUI设计、多线程编程、系统集成等高级特性！

### 🌍 核心功能
- **多语言翻译**: 支持中文、英文、日文、法文、德文等多语言互译
- **英文润色**: 将英文文本优化为更自然的Native Speaker表达
- **邮件撰写**: 根据原邮件内容和中文补充信息自动撰写专业邮件回复
- **自由对话**: 与AI进行自由对话交流

### 🔧 API支持
- **OpenAI**: 技术最成熟，英文处理最佳
- **DeepSeek**: 价格便宜，中文支持优秀，国内访问稳定
- **自定义API**: 支持其他兼容OpenAI格式的AI服务

### 💡 便捷特性
- **双模式运行**: 简单模式（最稳定）+ 完整模式（功能最全）
- **友好界面**: 直观的图形用户界面
- **一键复制**: 自动复制处理结果到剪贴板
- **配置保存**: 自动保存API密钥和用户偏好设置
- **多API切换**: 运行时随时切换不同的AI服务商

## 🚀 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置API密钥
- 运行程序后在界面中选择API提供商（OpenAI/DeepSeek/自定义）
- 输入对应的API密钥并保存

### 3. 启动程序

**🌟 推荐启动方式**:
```bash
# 完整模式（推荐）- 系统托盘 + 全局热键 + GUI
python main.py

# 使用方法：
# 🔹 右键点击托盘图标 → 选择"🚀 点我打开翻译器"
# 🔹 使用热键：Ctrl+Shift+T
# 🔹 尝试双击托盘图标（部分系统可能不响应）

# 或使用批处理脚本
.\start.bat
```

**🔧 其他启动方式**:
```bash
# 热键模式 - 仅全局热键，无托盘
python main_hotkey_only.py

# 简单模式 - 纯GUI，最大兼容性
python main_simple.py

# 交互式选择模式
.\start.bat
```

> **注意**: Python 3.13下推荐使用简单模式以确保最佳稳定性。

## 📊 模式对比

| 功能 | 简单模式 | 热键模式 | 完整模式 |
|------|:--------:|:--------:|:--------:|
| 文本翻译 | ✅ | ✅ | ✅ |
| 英文润色 | ✅ | ✅ | ✅ |
| 邮件撰写 | ✅ | ✅ | ✅ |
| 自由对话 | ✅ | ✅ | ✅ |
| 多API支持 | ✅ | ✅ | ✅ |
| 配置管理 | ✅ | ✅ | ✅ |
| GUI界面 | ✅ | ✅ | ✅ |
| 全局热键 | ❌ | ✅ | ✅ |
| 系统托盘 | ❌ | ❌ | ✅ |
| **稳定性** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **推荐度** | 基础用户 | 键盘党 | **完整体验** |

## 🛠️ 系统要求

- Python 3.13 或更高版本
- Windows 操作系统
- 网络连接（用于API调用）

## 📚 文档

- [快速开始指南](QUICKSTART.md)
- [快速开始指南-Docker](QUICKSTART-Docker.md)
- [用户使用指南](USER_GUIDE.md)
- [API切换指南](API_SWITCHING_GUIDE.md)
- [DeepSeek配置指南](DEEPSEEK_GUIDE.md)
- [Python 3.13兼容性说明](PYTHON313_COMPATIBILITY.md)

## 🔄 版本信息

当前版本: **v1.0.0** - 查看 [VERSION.md](VERSION.md) 了解更多

## 🤝 贡献

欢迎提交问题和改进建议！

## 📄 许可证

MIT License

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

**🤖 AI生成的技术栈**:
- **GUI框架**: Tkinter (AI选择的跨平台GUI解决方案)
- **API客户端**: OpenAI Python库 (AI集成的多服务商支持)
- **系统托盘**: pystray (AI解决了Python 3.13兼容性问题)
- **全局热键**: keyboard (AI实现的系统级热键注册)
- **剪贴板**: pyperclip (AI添加的便捷功能)
- **打包工具**: PyInstaller (AI配置的可执行文件生成)
- **线程管理**: 自定义线程架构 (AI设计的GIL问题解决方案)

## 🤖 AI开发声明

**这是一个完全由AI自动生成的项目！**

### 开发过程
- **编程助手**: GitHub Copilot + Claude 4 Sonnet
- **开发模式**: 100% AI代码生成，无人工编写代码
- **涵盖范围**: 
  - ✅ 完整的Python应用程序架构设计
  - ✅ GUI界面开发（Tkinter）
  - ✅ 系统托盘和全局热键功能
  - ✅ 多线程编程和异常处理
  - ✅ Python 3.13兼容性问题解决
  - ✅ 配置管理和数据持久化
  - ✅ 完整的项目文档和用户指南
  - ✅ Git版本控制和项目管理

### AI解决的技术难题
1. **Python 3.13 GIL线程问题**: AI自动诊断并解决了pystray库在Python 3.13下的线程冲突
2. **跨平台兼容性**: 自动处理Windows系统托盘和热键注册
3. **错误处理机制**: 全面的异常捕获和用户友好的错误提示
4. **代码架构优化**: 模块化设计，支持多种运行模式

### 展示AI编程能力
- **问题诊断**: 能够分析复杂的系统级错误和兼容性问题
- **解决方案**: 提供多种备选方案适应不同用户需求
- **代码质量**: 生成的代码结构清晰，注释详细，符合最佳实践
- **文档完整**: 自动生成用户指南、API文档、故障排除指南

> **致开发者**: 这个项目证明了AI在软件开发中的巨大潜力。从概念到成品，AI可以独立完成复杂的桌面应用程序开发，包括解决实际的技术难题。这为未来的软件开发模式提供了新的可能性！

## 开发者

项目地址: https://github.com/YangZeCN/SimpleTranslator

## 许可证

MIT License
