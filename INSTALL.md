# 安装指南

## 快速开始

### 1. 自动安装（推荐）
双击运行 `start.bat` 文件，脚本会自动：
- 检查Python环境
- 安装所需依赖包
- 启动程序

### 2. 手动安装

#### 步骤1: 安装Python依赖
```bash
pip install -r requirements.txt
```

#### 步骤2: 运行程序
```bash
python main.py
```

## 构建exe文件

### 使用构建脚本（推荐）
```bash
python build.py
```
选择选项3进行完整构建

### 手动构建
```bash
# 安装PyInstaller
pip install pyinstaller

# 构建exe
pyinstaller --onefile --windowed --name SimpleTranslator main.py
```

## 依赖包说明

- **openai**: OpenAI API客户端
- **pystray**: 系统托盘图标
- **pillow**: 图像处理（托盘图标）
- **keyboard**: 全局热键支持
- **pyperclip**: 剪贴板操作
- **tkinter**: GUI界面（Python内置）

## 常见问题

### Q: 提示"Import openai could not be resolved"
A: 运行 `pip install openai` 安装OpenAI包

### Q: 热键不生效
A: 某些系统可能需要以管理员权限运行程序

### Q: 构建exe失败
A: 确保已安装PyInstaller: `pip install pyinstaller`

### Q: API调用失败
A: 检查网络连接和API密钥是否正确

## 获取OpenAI API密钥

1. 访问 https://platform.openai.com/
2. 注册/登录账户
3. 进入 API Keys 页面
4. 创建新的API密钥
5. 复制密钥到程序配置中

## 技术支持

如遇到问题，请检查：
1. Python版本（建议3.8+）
2. 网络连接
3. API密钥有效性
4. 依赖包是否正确安装
