# XiaoYuanKouSuan_Auto

用于小猿口算的基于 Python 的自动答题工具（OCR 视觉识别）

[![Contributors](https://img.shields.io/github/contributors/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square)](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/pulse)
[![Forks](https://img.shields.io/github/forks/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square)](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/network/members)
[![Stars](https://img.shields.io/github/stars/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square)](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/stargazers)
[![Issues](https://img.shields.io/github/issues/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square)](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/issues)
[![License](https://img.shields.io/github/license/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square)](LICENSE)

---

## 📌 项目简介

**“小猿口算自动答题器”**

用于 **小猿口算** 的 Python 自动化答题工具，  
基于 **Tesseract OCR 文本识别 + 模拟人工输入** 实现。

> 本项目不会修改或注入小猿口算任何程序数据，  
> 仅通过 **屏幕识别 + 自动化交互** 完成操作。

本人对 **B 站锁定相关技术演示视频** 表示抗议  
（BV1kc2NY6Ey1）

![image](https://github.com/user-attachments/assets/7b3c2c67-7e7c-4a38-a972-3c572617dced)

🔗 项目地址：  
👉 https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto

---

## 📚 目录

- [上手指南](#上手指南)
- [开发前的配置要求](#开发前的配置要求)
- [安装步骤](#安装步骤)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
- [作者](#作者)
- [版权说明](#版权说明)
- [鸣谢](#鸣谢)

---

## 🚀 上手指南

- 使用 **BlueStacks 模拟器** 运行 Android 虚拟机  
- 通过 **BlueStacks 脚本管理器** 录制 `>` `<` 手写输入  
- 设置为 **5 倍速**
- 绑定热键：
  - `.` → `>`
  - `,` → `<`

示例图：

![example2](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/blob/main/image/example2.png)

示例代码：

```python
def draw_greater_than(origin_x, origin_y, size):
    pyautogui.press(".")

def draw_less_than(origin_x, origin_y, size):
    pyautogui.press(",")
````

---

## ⚙️ 开发前的配置要求

1. Python **3.12.5**
2. Tesseract OCR（需安装中文语言包 `chi_sim`）
3. Windows 系统（仅支持 Windows）

---

## 📦 安装步骤

### 1️⃣ 安装 Python

[https://www.python.org/](https://www.python.org/)

---

### 2️⃣ 安装 Tesseract OCR（Windows）

[https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
请确保安装 **中文语言包**

---

### 3️⃣ 下载脚本文件

👉
[https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/blob/main/%E5%B0%8F%E7%8C%BF%E6%90%9C%E9%A2%98.py](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/blob/main/%E5%B0%8F%E7%8C%BF%E6%90%9C%E9%A2%98.py)

---

### 4️⃣ 安装依赖库

清华源（推荐）：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python numpy pyautogui pytesseract keyboard
```

官方源：

```bash
pip install opencv-python numpy pyautogui pytesseract keyboard
```

---

### 5️⃣ 配置 Tesseract 路径

修改脚本第 9 行：

![example3](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/blob/main/image/example3.png)

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

### 6️⃣ 调整识别区域

根据你实际屏幕位置调整坐标：

![example1](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/blob/main/image/example1.png)

---

## 🧰 使用到的框架

* Python
* Tesseract OCR
* OpenCV
* PyAutoGUI

---

## 👤 作者

ChaosJulien
📧 [ChaosJulien@163.com](mailto:ChaosJulien@163.com)

---

## 📄 版权说明

本项目基于 **MIT License**
详见 [LICENSE](LICENSE)

---

## 🙏 鸣谢

* GitHub Emoji Cheat Sheet
* Shields.io
* Choose an Open Source License
* GitHub Pages
