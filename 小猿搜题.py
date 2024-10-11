import cv2
import numpy as np
import pyautogui
import pytesseract
import keyboard
import sys
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # 设置 Tesseract-OCR 的路径

# 跟踪状态的变量
not_found_count = 0
last_not_found_time = 0
last_numbers = None  # 存储上次识别的数字
skip_count = 0  # 跳过次数计数器

def capture_area():
    region = (84, 336, 411, 55)  # (x, y, width, height) 详情如何配置可以看 (https://github.com/ChaosJulien/XiaoYuanKouSuan_Auto/blob/main/image/example1.png)
    screenshot = pyautogui.screenshot(region=region)
    return np.array(screenshot)

def recognize_numbers(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 6')
    return [int(s) for s in text.split() if s.isdigit()]

def handle_insufficient_numbers():
    global not_found_count, last_not_found_time

    current_time = time.time()
    not_found_count = not_found_count + 1 if current_time - last_not_found_time <= 1 else 1
    last_not_found_time = current_time

    print("未找到足够的数字进行比较")
    if not_found_count >= 25:
        click_buttons()
        time.sleep(13)
        print("准备重新开始程序...")
        time.sleep(0.3)
        main()

def click_buttons():
    pyautogui.click(280, 840)  # 点击“开心收下”按钮
    time.sleep(0.3)
    pyautogui.click(410, 990)  # 点击“继续”按钮
    time.sleep(0.3)
    pyautogui.click(280, 910)  # 点击“继续PK”按钮

def draw_comparison(numbers):
    global not_found_count, last_numbers, skip_count

    if len(numbers) < 2:
        handle_insufficient_numbers()
        return

    # 如果当前数字与上一个数字相同，则增加跳过计数
    if last_numbers is not None and last_numbers == numbers:
        skip_count += 1
        print(f"当前结果与上次相同，跳过此次执行 (次数: {skip_count})")
        if skip_count > 5:  # 如果跳过次数超过5，则强制执行一次
            skip_count = 0
            execute_drawing_logic(numbers)
        return

    execute_drawing_logic(numbers)  # 执行当前数字的绘制逻辑

    not_found_count = 0  # 重置未找到计数
    last_numbers = numbers  # 更新上次识别的数字
    skip_count = 0  # 重置跳过次数

def execute_drawing_logic(numbers):
    first, second = numbers[:2]  # 获取前两个数字
    print(f"识别的数字: {first}, {second}")

    if first > second:
        print(f"{first} > {second}")
        draw_greater_than()
    elif first < second:
        print(f"{first} < {second}")
        draw_less_than()

def draw_greater_than():
    pyautogui.press(".")  # BlueStacks中的大于号快捷键

def draw_less_than():
    pyautogui.press(",")  # BlueStacks中的小于号快捷键

def main():
    keyboard.add_hotkey('=', lambda: sys.exit("进程已结束"))  # 默认的退出快捷键

    try:
        while True:
            image = capture_area()  # 截取屏幕区域
            numbers = recognize_numbers(image)  # 从截取的图像中识别数字
            draw_comparison(numbers)  # 比较并绘制结果
           # time.sleep(0.01)
    except SystemExit as e:
        print(e)

if __name__ == "__main__":
    main()  # 启动主程序
