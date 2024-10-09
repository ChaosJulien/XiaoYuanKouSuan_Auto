import cv2
import numpy as np
import pyautogui
import pytesseract
import keyboard
import sys
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

not_found_count = 0
last_not_found_time = 0

def capture_area():
    region = (60, 260, 360, 320)  # (x, y, width, height) 坐标是由上到下，由左到右的;此坐标是识别区域坐标 左上:(60,260) 右下:(360,320)
    screenshot = pyautogui.screenshot(region=region)
    return np.array(screenshot)

def recognize_numbers(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 6')
    numbers = [int(s) for s in text.split() if s.isdigit()]
    return numbers

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

            pyautogui.click(218, 651) # 此坐标是“开心收下”按钮的坐标
            time.sleep(0.3)
            pyautogui.click(313, 956) # 此坐标是“继续”按钮的坐标
            time.sleep(0.3)
            pyautogui.click(219, 844) # 此坐标是“继续PK”按钮的坐标
            time.sleep(13)
            
            print("准备重新开始程序...")
            time.sleep(1)
            main()
        return

    first, second = numbers[0], numbers[1]
    origin_x, origin_y = 250, 650  # 此坐标是绘制区域是坐标
    size = 50

    if first > second:
        print(f"{first} > {second}")
        draw_greater_than(origin_x, origin_y, size)
    elif first < second:
        print(f"{first} < {second}")
        draw_less_than(origin_x, origin_y, size)

    not_found_count = 0  

def draw_greater_than(origin_x, origin_y, size):
    pyautogui.mouseDown(origin_x, origin_y)
    pyautogui.moveTo(origin_x + size, origin_y + size, duration=0.02)
    pyautogui.moveTo(origin_x, origin_y + size, duration=0.02)
    pyautogui.mouseUp()

def draw_less_than(origin_x, origin_y, size):
    pyautogui.mouseDown(origin_x + size, origin_y)
    pyautogui.moveTo(origin_x, origin_y + size, duration=0.02)
    pyautogui.moveTo(origin_x + size, origin_y + size, duration=0.02)
    pyautogui.mouseUp()

def main():
    keyboard.add_hotkey('=', lambda: sys.exit("进程已结束")) #默认退出快捷键是“=”

    try:
        while True:
            image = capture_area()
            numbers = recognize_numbers(image)
            draw_comparison(numbers)
            time.sleep(0.3) # 每次绘画及识别的延迟
    except SystemExit as e:
        print(e)

if __name__ == "__main__":
    main()
