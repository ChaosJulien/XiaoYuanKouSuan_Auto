

# XiaoYuanKouSuan_Auto

用于小猿口算的基于Python的自动答题工具


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />

<p align="center">

  <h3 align="center">“小猿口算自动答题器”</h3>
  <p align="center">
    用于小猿口算的基于Python的自动答题工具
    <br />
    <a href="https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto"><strong>探索本项目的文档 »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/issues">报告Bug</a>
    ·
    <a href="https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/issues">提出新特性</a>
  </p>

</p>

 
## 目录

- [上手指南](#上手指南)
  - [开发前的配置要求](#开发前的配置要求)
  - [安装步骤](#安装步骤)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
  - [如何参与开源项目](#如何参与开源项目)
- [作者](#作者)
- [鸣谢](#鸣谢)

### 上手指南
使用`BlueStacks`模拟器运行Android虚拟机 </br>
使用`BlueStacks脚本管理器`手写录入`>` `<`的输入内容并调整至5倍速 </br>
![](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/blob/main/image/example2.png) </br>
将其绑定热键至`,` `.` </br>
```python
def draw_greater_than(origin_x, origin_y, size):
    pyautogui.press(".")

def draw_less_than(origin_x, origin_y, size):
    pyautogui.press(",")
```


>请确保基于Windows进行编译 </br>
 拥有一台有MIUI+或小米妙想功能的手机</br>
 桌面操作系统中安装了MIUI+或小米电脑管家，并能成功将手机投屏至桌面端</br>

###### 开发前的配置要求

1. 本项目基于Python 3.12.5进行开发
2. 本项目使用了tesseract文本识别(OCR)引擎

###### **安装步骤**

1. 在[Python](https://www.python.org/) 下载对应Python版本
2. 在[tesseract](https://github.com/tesseract-ocr/tesseract)下载Windows版本，并安装中文语言确保最佳兼容性
3. 下载[小猿搜题.py](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/blob/main/%E5%B0%8F%E7%8C%BF%E6%90%9C%E9%A2%98.py)
4. 安装所需的Python库
```python
pip install opencv-python pyautogui pytesseract keyboard numpy
```
5. 调整第9行代码路径为你的tesseract安装路径
6. 根据你的所属位置进行调整,如下图所示 </br>
![](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/blob/main/image/example1.png)


### 使用到的框架

- [Python](https://www.python.org/)
- [tesseract][(https://github.com/tesseract-ocr/tesseract)

### 贡献者

请阅读**CONTRIBUTING.md** 查阅为该项目做出贡献的开发者。

#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



### 作者

ChaosJulien@163.com

### 版权说明

该项目签署了GNU通用公共许可证，详情请参阅 [LICENSE](https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/LICENSE)

### 鸣谢


- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)
- [Animate.css](https://daneden.github.io/animate.css)
- [xxxxxxxxxxxxxx](https://connoratherton.com/loaders)

<!-- links -->
[your-project-path]:/ChaosJulien/XiaoYuanKouSuan_Auto
[contributors-shield]: https://img.shields.io/github/contributors/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square
[contributors-url]: https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/pulse
[forks-shield]: https://img.shields.io/github/forks/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square
[forks-url]: https://github.com//ChaosJulien/XiaoYuanKouSuan_Auto/network/members
[stars-shield]: https://img.shields.io/github/stars/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square
[stars-url]: https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/stargazers
[issues-shield]: https://img.shields.io/github/issues/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square
[issues-url]: https://img.shields.io/github/issues/shaojintian/Best_README_template.svg
[license-shield]: https://img.shields.io/github/license/ChaosJulien/XiaoYuanKouSuan_Auto.svg?style=flat-square
[license-url]: https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/LICENSE



