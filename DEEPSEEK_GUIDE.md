# DeepSeek API 配置指南

## 🚀 DeepSeek API 简介

DeepSeek是一家中国的AI公司，提供高质量的语言模型服务。相比OpenAI，DeepSeek的优势包括：

- ✅ **价格更便宜**：相同功能下成本更低
- ✅ **中文支持更好**：对中文理解和生成更优秀
- ✅ **访问更稳定**：国内访问速度更快
- ✅ **兼容OpenAI API**：无需修改代码即可切换

## 📝 如何获取DeepSeek API密钥

### 步骤1：注册账号
1. 访问 [DeepSeek官网](https://www.deepseek.com/)
2. 点击"登录/注册"
3. 使用手机号或邮箱注册账号

### 步骤2：获取API密钥
1. 登录后进入[API控制台](https://platform.deepseek.com/)
2. 点击"API Keys"
3. 点击"Create API Key"
4. 设置密钥名称（如"SimpleTranslator"）
5. 复制生成的API密钥

### 步骤3：充值（如需要）
1. 在控制台点击"充值"
2. 选择充值金额
3. 支持支付宝、微信支付

## ⚙️ 在SimpleTranslator中配置DeepSeek

### 方法1：通过界面配置（推荐）
1. 启动SimpleTranslator
2. 按 `Ctrl+Shift+T` 打开界面
3. 在"API提供商"下拉框中选择"deepseek"
4. 在"API Key"框中输入你的DeepSeek API密钥
5. 点击"保存配置"

### 方法2：直接编辑配置文件
编辑 `config.json` 文件：
```json
{
  "api_provider": "deepseek",
  "deepseek_api_key": "你的DeepSeek API密钥",
  "deepseek_model": "deepseek-chat"
}
```

## 🎯 DeepSeek支持的模型

SimpleTranslator默认使用 `deepseek-chat` 模型，这是DeepSeek的主力对话模型，适合：
- 文本翻译
- 内容润色
- 邮件撰写
- 自由对话

如需使用其他模型，可以在 `config.json` 中修改 `deepseek_model` 字段。

## 💰 价格对比

| 服务商 | 模型 | 输入价格（1M tokens） | 输出价格（1M tokens） |
|--------|------|----------------------|----------------------|
| OpenAI | GPT-3.5-turbo | $0.50 | $1.50 |
| DeepSeek | deepseek-chat | ¥1.00 | ¥2.00 |

*价格仅供参考，请以官方最新价格为准*

## 🔄 API提供商切换

SimpleTranslator支持在以下API提供商之间自由切换：

### OpenAI（原版）
- **优势**：技术最成熟，英文处理最佳
- **劣势**：价格较高，国内访问可能不稳定
- **适用场景**：英文润色、复杂推理任务

### DeepSeek（推荐）
- **优势**：价格便宜，中文优秀，访问稳定
- **劣势**：技术相对较新
- **适用场景**：中文翻译、日常对话、邮件撰写

### 自定义API
- **适用于**：其他兼容OpenAI API格式的服务
- **如**：本地部署的模型、其他AI服务商

## 🛠️ 故障排除

### Q: DeepSeek API调用失败？
A: 检查以下几点：
1. API密钥是否正确
2. 账户余额是否充足
3. 网络连接是否正常
4. API配额是否用完

### Q: 如何查看API使用情况？
A: 登录DeepSeek控制台，在"使用情况"页面查看详细统计

### Q: 可以同时配置多个API吗？
A: 可以！程序会保存所有API的密钥，随时可以切换使用

## 🎉 开始使用

配置完成后，你就可以享受DeepSeek带来的高质量、低成本AI服务了！特别是中文相关任务，DeepSeek的表现可能会让你惊喜。
