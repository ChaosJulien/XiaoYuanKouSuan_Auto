# XiaoYuanKouSuan_Auto

用于 **小猿口算** 的 Python 自动答题辅助工具（基于 OCR 视觉识别）

[![Contributors](https://img.shields.io/github/contributors/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square)](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/pulse)
[![Forks](https://img.shields.io/github/forks/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square)](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/network/members)
[![Stars](https://img.shields.io/github/stars/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square)](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/stargazers)
[![Issues](https://img.shields.io/github/issues/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square)](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/issues)
[![License](https://img.shields.io/github/license/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square)](LICENSE)

---

## 📌 项目简介

**XiaoYuanKouSuan_Auto** 是一个基于 **Python + Tesseract OCR** 的视觉识别自动答题工具，  
通过 **屏幕识别 + 自动化输入** 的方式，辅助完成小猿口算中的简单算术与大小比较题目。

> ⚠️ **重要说明**
>
> - 本项目 **不会修改、注入或篡改** 小猿口算客户端或服务器数据  
> - 所有操作均基于 **模拟器画面识别与人工交互模拟**
> - 本项目仅用于 **技术研究 / OCR / 自动化实验学习**
> - **禁止用于商业用途或恶意刷榜行为**
> - 使用本项目所产生的一切后果 **由使用者自行承担**

---

## 🧩 功能特性

- 📷 基于 **Tesseract OCR** 的题目识别
- ➕➖✖➗ 支持基础算术识别
- 🔺🔻 支持 `>` `<` 比较题（通过按键映射）
- 🖥 适配 **BlueStacks 模拟器**
- ⚡ 快速自动输入，减少重复操作

---

## 🧰 运行环境要求

### 系统要求
- Windows 10 / 11（**仅支持 Windows**）
- 推荐使用 **BlueStacks 模拟器**

### Python 环境
- Python **3.12.x**（开发版本：3.12.5）

### 依赖组件
- Tesseract OCR（需安装中文语言包）

---

## 🚀 安装与配置

### 1️⃣ 安装 Python
前往官网下载并安装：
👉 https://www.python.org/

安装时请勾选 **Add Python to PATH**

---

### 2️⃣ 安装 Tesseract OCR（Windows）

下载地址：
👉 https://github.com/tesseract-ocr/tesseract

安装时请注意：
- 勾选 **中文语言包（chi_sim）**
- 记住安装路径（后续要用）

---

### 3️⃣ 下载项目脚本

直接下载主脚本文件：

👉 [小猿搜题.py](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/blob/main/%E5%B0%8F%E7%8C%BF%E6%90%9C%E9%A2%98.py)

本项目为 **单文件脚本，无需额外工程结构**

---

### 4️⃣ 安装 Python 依赖库

#### 推荐（清华大学镜像，速度快）
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python numpy pyautogui pytesseract keyboard
````

#### 官方源

```bash
pip install opencv-python numpy pyautogui pytesseract keyboard
```

---

### 5️⃣ 配置 Tesseract 路径

打开 `小猿搜题.py`，修改以下路径为你本地的 Tesseract 安装路径：

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

### 6️⃣ BlueStacks 输入映射设置

* 使用 **BlueStacks 脚本管理器**
* 录制手写输入 `>` 与 `<`
* 设置为 **5 倍速**
* 绑定热键：

  * `.` → `>`
  * `,` → `<`

示例代码：

```python
def draw_greater_than(origin_x, origin_y, size):
    pyautogui.press(".")

def draw_less_than(origin_x, origin_y, size):
    pyautogui.press(",")
```

---

## 🧠 技术原理简述

1. 截取模拟器指定区域画面
2. 使用 OpenCV 预处理图像
3. 通过 Tesseract OCR 识别算式文本
4. Python 解析并计算结果
5. 使用 PyAutoGUI 模拟人工输入

---

## 🤝 参与贡献

欢迎提交 Issue / PR：

1. Fork 本项目
2. 创建功能分支

   ```bash
   git checkout -b feature/YourFeature
   ```
3. 提交修改

   ```bash
   git commit -m "Add YourFeature"
   ```
4. 推送并发起 Pull Request

---

## 👤 作者

**ChaosJulien**
📧 [ChaosJulien@163.com](mailto:ChaosJulien@163.com)
GitHub: [https://github.com/ChaosJulien](https://github.com/ChaosJulien)

---

## 📄 许可证

本项目基于 **MIT License** 开源
详见 [LICENSE](LICENSE)

---

## 🙏 鸣谢

* Tesseract OCR
* OpenCV
* PyAutoGUI
* GitHub Shields
* 所有为本项目提出建议和 Issue 的朋友

```
