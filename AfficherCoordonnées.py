import pyautogui, keyboard

while not keyboard.is_pressed('q'):
    if keyboard.is_pressed('x'):
        print(pyautogui.position())