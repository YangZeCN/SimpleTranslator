# API 切换使用示例

## 🔄 快速切换API提供商

### 通过界面切换（推荐）

1. **启动程序**
   ```bash
   py -3.13 main.py
   ```

2. **打开界面**
   - 按 `Ctrl+Shift+T`

3. **切换API提供商**
   - 在"API提供商"下拉框中选择：
     - `openai` - 使用OpenAI GPT
     - `deepseek` - 使用DeepSeek（推荐）
     - `custom` - 使用自定义API

4. **输入对应密钥**
   - 程序会自动加载对应提供商的已保存密钥
   - 如果是首次使用，需要输入新密钥

5. **保存配置**
   - 点击"保存配置"按钮

### 通过配置文件切换

编辑 `config.json`：

```json
{
  "api_provider": "deepseek",          // 切换到DeepSeek
  "deepseek_api_key": "sk-your-key"   // 确保有对应的密钥
}
```

## 💡 使用建议

### OpenAI 适用场景
- ✅ 复杂的英文写作和润色
- ✅ 专业学术翻译
- ✅ 复杂的逻辑推理
- ❌ 成本考虑（价格较高）

### DeepSeek 适用场景
- ✅ 中文翻译和对话
- ✅ 日常邮件撰写
- ✅ 成本敏感的应用
- ✅ 国内用户（访问稳定）

### 自定义API 适用场景
- ✅ 使用其他AI服务商
- ✅ 本地部署的模型
- ✅ 企业内部API

## 🎯 最佳实践

### 1. 按任务类型选择API
```
中文翻译 → DeepSeek
英文润色 → OpenAI
日常对话 → DeepSeek
专业翻译 → OpenAI
```

### 2. 成本优化策略
- 日常使用：DeepSeek
- 重要文档：OpenAI
- 可以同时配置多个API，按需切换

### 3. 配置示例

**多API同时配置**：
```json
{
  "api_provider": "deepseek",
  "openai_api_key": "sk-openai-key-here",
  "deepseek_api_key": "sk-deepseek-key-here",
  "custom_api_key": "custom-key-here",
  "custom_base_url": "https://api.example.com/v1",
  "model": "gpt-3.5-turbo",
  "deepseek_model": "deepseek-chat",
  "custom_model": "llama-2-7b-chat"
}
```

这样配置后，你可以随时在界面中切换使用不同的API，而无需重新输入密钥。

## 🚀 开始使用

现在你已经了解如何在不同的AI服务之间切换了！

1. 配置你想要的API服务
2. 根据任务选择最适合的提供商
3. 享受多样化的AI服务带来的便利

**推荐新用户**：先从DeepSeek开始，价格便宜且中文表现优秀！
