import easyocr, time, pyautogui
#reader = easyocr.Reader(['en'], gpu=False)

def lire_monument(reader):
    text_ = reader.readtext('screenshot.png')
    return text_[1][1]

print("go")
#print(lire_monument(reader))
def replay():
    time.sleep(1)
    pyautogui.press('f5')
    time.sleep(1)
    pyautogui.scroll(15000)
    time.sleep(0.2)
    pyautogui.scroll(-900)
    time.sleep(0.2)
    pyautogui.click((949, 643))
    time.sleep(0.2)

replay()