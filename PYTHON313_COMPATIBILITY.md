# Python 3.13 兼容性问题解决方案

## 🐛 问题描述

在Python 3.13中运行SimpleTranslator时可能出现以下错误：
```
Fatal Python error: PyEval_RestoreThread: the function must be called with the GIL held...
```

这是由于Python 3.13对多线程和GIL（全局解释器锁）的改进导致的兼容性问题。

## ✅ 解决方案

我们提供了多种启动模式来解决此问题：

### 方案1：简单模式（推荐）

**特点**：
- ✅ 最稳定，无多线程问题
- ✅ 包含所有核心翻译功能
- ❌ 没有系统托盘功能
- ❌ 没有全局热键

**启动方式**：
```bash
# 直接运行
py -3.13 main_simple.py

# 或使用批处理文件
start_simple.bat
```

### 方案2：完整模式（修复后）

**特点**：
- ✅ 包含所有功能（系统托盘、热键）
- ⚠️ 在某些系统上可能不稳定

**启动方式**：
```bash
# 直接运行
py -3.13 main.py

# 或使用批处理文件
start_full.bat
```

### 方案3：交互式选择

使用主启动脚本，可以选择启动模式：
```bash
start.bat
```

## 🎯 推荐使用方案

### 新用户或追求稳定性
→ **使用简单模式**（`start_simple.bat`）

### 需要全功能体验
→ **先试完整模式**（`start_full.bat`），如有问题再用简单模式

## 🔧 两种模式功能对比

| 功能 | 简单模式 | 完整模式 |
|------|----------|----------|
| 文本翻译 | ✅ | ✅ |
| 英文润色 | ✅ | ✅ |
| 邮件撰写 | ✅ | ✅ |
| 自由对话 | ✅ | ✅ |
| 多API支持 | ✅ | ✅ |
| GUI界面 | ✅ | ✅ |
| 系统托盘 | ❌ | ✅ |
| 全局热键 | ❌ | ✅ |
| 后台运行 | ❌ | ✅ |

## 📁 启动文件说明

```
start.bat         - 交互式选择启动模式
start_simple.bat  - 直接启动简单模式（推荐）
start_full.bat    - 直接启动完整模式
main_simple.py    - 简单模式主程序
main.py          - 完整模式主程序
```

## 🛠️ 进一步的解决方案

如果仍然遇到问题，可以尝试：

### 1. 降级Python版本
```bash
# 安装Python 3.11或3.12
# 这些版本没有此兼容性问题
```

### 2. 更新依赖包
```bash
pip install --upgrade pystray keyboard pillow
```

### 3. 使用虚拟环境
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 🎉 总结

- **简单模式**：最稳定的选择，适合日常使用
- **完整模式**：功能最全，但可能在某些系统不稳定
- **建议**：优先使用简单模式，核心功能完全相同

无论选择哪种模式，所有的翻译功能和API切换功能都完全可用！
