import pyautogui, keyboard

while not keyboard.is_pressed('q'):
    if keyboard.is_pressed('x'):
        screenshot = pyautogui.screenshot()
        img = screenshot.convert("RGB")
        pixel_color = img.getpixel(pyautogui.position())
        print(pixel_color)