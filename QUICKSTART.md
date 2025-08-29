# 快速开始指南

## 🚀 如何启动程序

你现在已经成功切换到Python 3.13并安装了所有依赖包！以下是启动程序的几种方法：

### 方法1: 直接运行Python脚本
```bash
py -3.13 main.py
```

### 方法2: 使用批处理脚本
双击 `start.bat` 文件，它会自动：
- 检测Python版本（优先使用3.13）
- 检查和安装依赖包
- 启动程序

### 方法3: 使用PowerShell脚本（推荐）
右键 `start.ps1` → "使用PowerShell运行"
- 更智能的Python版本检测
- 更好的错误处理
- 彩色输出显示

## 📋 首次使用设置

### 选择API提供商

SimpleTranslator支持多种AI服务：

#### 1. **OpenAI（原版）**
- 访问 https://platform.openai.com/api-keys
- 创建API密钥
- 技术最成熟，英文处理最佳

#### 2. **DeepSeek（推荐国内用户）**
- 访问 https://platform.deepseek.com/
- 注册并获取API密钥
- 价格便宜，中文支持优秀，访问稳定
- 详细配置请参考 `DEEPSEEK_GUIDE.md`

#### 3. **自定义API**
- 支持其他兼容OpenAI格式的AI服务
- 需要提供Base URL、API密钥和模型名称

### 配置程序
1. 启动程序后，程序会在系统托盘运行
2. 使用快捷键 `Ctrl+Shift+T` 打开界面
3. 选择API提供商（openai/deepseek/custom）
4. 输入对应的API密钥
5. 如果选择自定义API，还需填写Base URL和模型名称
6. 点击"保存配置"

## 🎯 主要功能

### 1. 文本翻译
- 选择"翻译"模式
- 选择目标语言（中文、英文、日文等）
- 输入要翻译的文本
- 点击"处理"

### 2. 英文润色
- 选择"英文润色"模式
- 输入需要优化的英文文本
- 程序会将其改写得更像Native Speaker

### 3. 邮件撰写
- 选择"邮件撰写"模式
- 在主输入框粘贴原邮件内容
- 在"附加信息"框输入中文补充说明
- 程序会生成专业的邮件回复

### 4. 自由对话
- 选择"自由对话"模式
- 与ChatGPT进行自由交流

## ⌨️ 快捷操作

- **全局热键**: `Ctrl+Shift+T` - 随时唤出程序界面
- **粘贴**: 快速将剪贴板内容粘贴到输入框
- **复制结果**: 将处理结果复制到剪贴板
- **系统托盘**: 程序最小化到系统托盘，右键查看菜单

## 🔧 高级配置

编辑 `config.json` 文件可以自定义：

### API提供商配置
```json
{
  "api_provider": "deepseek",           // 当前使用的API提供商
  "openai_api_key": "sk-xxx",          // OpenAI API密钥
  "deepseek_api_key": "sk-xxx",        // DeepSeek API密钥
  "custom_api_key": "xxx",             // 自定义API密钥
  "custom_base_url": "https://xxx",    // 自定义API地址
  "model": "gpt-3.5-turbo",            // OpenAI模型
  "deepseek_model": "deepseek-chat",   // DeepSeek模型
  "custom_model": "custom-model"       // 自定义模型
}
```

### 其他配置
- 最大token数量
- 温度参数（创造性）
- 热键组合
- 窗口大小等

## 📦 打包成exe

如果想要创建独立的exe文件：

1. 运行构建脚本：
   ```bash
   py -3.13 build.py
   ```

2. 选择选项3进行完整构建

3. 生成的exe文件位于 `dist/SimpleTranslator.exe`

## ❗ 注意事项

1. **API费用**: 
   - OpenAI：相对较贵，但技术最成熟
   - DeepSeek：价格便宜，中文优秀
   - 请根据需求选择合适的服务商
2. **网络连接**: 程序需要网络连接调用API
3. **隐私保护**: 输入的文本会发送到对应的AI服务器处理
4. **热键冲突**: 如果热键不生效，可能与其他软件冲突
5. **管理员权限**: 某些情况下可能需要管理员权限运行

## 🆘 常见问题

**Q: 程序启动后看不到界面？**
A: 程序启动后在系统托盘运行，使用Ctrl+Shift+T唤出界面

**Q: API调用失败？**
A: 检查网络连接、API密钥是否正确、账户余额是否充足

**Q: DeepSeek和OpenAI哪个更好？**
A: DeepSeek价格便宜且中文优秀，OpenAI技术最成熟。建议中文任务用DeepSeek，英文任务用OpenAI

**Q: 可以同时配置多个API吗？**
A: 可以！程序会保存所有API密钥，可以随时切换使用

**Q: 热键不生效？**
A: 尝试以管理员权限运行程序

**Q: 依赖安装失败？**
A: 检查网络连接，可能需要配置pip镜像源

## 🎉 开始使用

现在你可以开始使用SimpleTranslator了！启动程序，配置API密钥，享受AI助手带来的便利吧！
