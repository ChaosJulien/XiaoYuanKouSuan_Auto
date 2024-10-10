import cv2
import numpy as np
import pyautogui
import pytesseract
import sys
import time
from pynput import keyboard
import Quartz.CoreGraphics as CG

# 设置Tesseract路径 (Mac)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

not_found_count = 0
last_not_found_time = 0


# 使用pyautogui截屏
def grab_screen(bbox):
    x, y, width, height = bbox
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # 保存截图以调试
    # screenshot.save(f"screenshot_debug_{time.time()}.png")

    return np.array(screenshot)


def capture_area():
    region = (230, 245, 165, 50)  # 定义截屏区域 (x, y, width, height)
    screenshot = grab_screen(region)

    # 返回numpy数组格式的截图
    return screenshot


import re


def recognize_numbers(image):
    # 将图像转换为灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 应用二值化处理
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

    # 进行形态学操作来分离相邻字符（防止 "11" 被误识别）
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # 提高对比度和锐度以增强数字边缘
    thresh = cv2.GaussianBlur(thresh, (1, 1), 0)
    thresh = cv2.convertScaleAbs(thresh, alpha=2.0, beta=0)

    # 保存处理后的图像以供调试
    # cv2.imwrite(f"thresh_debug_{time.time()}.png", thresh)

    # 获取图像的宽度和高度
    h, w = thresh.shape

    # 裁剪左右部分，忽略中间50像素宽的区域
    left_part = thresh[:, :w // 2 - 25]  # 左边部分
    right_part = thresh[:, w // 2 + 25:]  # 右边部分

    # 使用Tesseract仅识别数字，并限制字符集为数字
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'

    # 识别左边部分的数字
    left_text = pytesseract.image_to_string(left_part, config=custom_config)
    # print(f"左边识别到的文本：{left_text}")
    left_numbers = re.findall(r'\d+', left_text)  # 提取左边的数字

    # 识别右边部分的数字
    right_text = pytesseract.image_to_string(right_part, config=custom_config)
    # print(f"右边识别到的文本：{right_text}")
    right_numbers = re.findall(r'\d+', right_text)  # 提取右边的数字

    # 将提取到的数字字符串转换为整数
    left_numbers = [int(num) for num in left_numbers]
    right_numbers = [int(num) for num in right_numbers]

    # 合并左右两边的数字到一个列表中
    numbers = left_numbers + right_numbers

    return numbers


# 根据数字进行比较并绘制符号
def draw_comparison(numbers):
    global not_found_count, last_not_found_time

    if len(numbers) < 2:
        current_time = time.time()
        if not_found_count == 0 or current_time - last_not_found_time > 1:
            not_found_count = 1
        else:
            not_found_count += 1

        last_not_found_time = current_time
        print("未找到足够的数字进行比较")

        if not_found_count >= 10:
            pyautogui.click(333, 483)  # “开心收下”按钮
            time.sleep(0.3)
            pyautogui.click(433, 945)  # “继续”按钮
            time.sleep(1.0)
            pyautogui.click(326, 818)  # “继续PK”按钮
            time.sleep(10)

            print("准备重新开始程序...")
            time.sleep(1)
            main()
        return

    first, second = numbers[0], numbers[1]
    origin_x, origin_y = 323, 693  # 手写栏的起始坐标
    size = 10

    if first > second:
        print(f"{first} > {second}")
        draw_greater_than(origin_x, origin_y, size)
    elif first < second:
        print(f"{first} < {second}")
        draw_less_than(origin_x, origin_y, size)

    not_found_count = 0


def mouse_event(type, posx, posy):
    event = CG.CGEventCreateMouseEvent(None, type, (posx, posy), CG.kCGMouseButtonLeft)
    CG.CGEventPost(CG.kCGHIDEventTap, event)


def mouse_click_down(posx, posy):
    mouse_event(CG.kCGEventLeftMouseDown, posx, posy)


def mouse_click_up(posx, posy):
    mouse_event(CG.kCGEventLeftMouseUp, posx, posy)


def mouse_drag(posx, posy):
    mouse_event(CG.kCGEventLeftMouseDragged, posx, posy)


# 绘制大于号
def draw_greater_than(origin_x, origin_y, size):
    # 按下鼠标
    mouse_click_down(origin_x, origin_y)
    time.sleep(0.03)

    # 一次性拖拽完成整个大于号
    mouse_drag(origin_x + size, origin_y + size)  # 从左上到右下
    time.sleep(0.03)
    mouse_drag(origin_x, origin_y + size)  # 从右下回到左下
    time.sleep(0.03)

    # 松开鼠标
    mouse_click_up(origin_x, origin_y + size)


# 绘制小于号
def draw_less_than(origin_x, origin_y, size):
    # 按下鼠标，从右上角开始
    mouse_click_down(origin_x + size, origin_y)
    time.sleep(0.03)

    # 拖拽至左下角
    mouse_drag(origin_x, origin_y + size)
    time.sleep(0.03)

    # 再从左下角拖拽到右下角
    mouse_drag(origin_x + size, origin_y + size)
    time.sleep(0.03)

    # 松开鼠标
    mouse_click_up(origin_x + size, origin_y + size)


# 停止程序的热键
def on_press(key):
    try:
        if key.char == '=':
            print("进程已结束")
            sys.exit()
    except AttributeError:
        pass


# 主函数
def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
        while True:
            image = capture_area()
            numbers = recognize_numbers(image)
            draw_comparison(numbers)
            time.sleep(0.3)  # 延迟
    except SystemExit as e:
        print(e)


if __name__ == "__main__":
    main()
