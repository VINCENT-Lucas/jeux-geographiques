from GeoPlayerV1 import *
print("DEBUT DE L'ENTRAINEMENT")

def detect(name: str, data):
    for elem in data.keys():
        if name[:25] == elem[:25]:
            return True

data = load_data("data.txt")
reader = easyocr.Reader(['en'], gpu=False)

while not keyboard.is_pressed('q'):
    if keyboard.is_pressed('x'):
        take_screenshot()
        pos = pyautogui.position()
        nom_monument = lire_monument(reader)
        if nom_monument not in data:
            print(f"{nom_monument} ***NOUVEAU***")
            data[nom_monument] = (pos.x, pos.y)

save_data(data, "data.txt")
print("FIN DE L'ENTRAINEMENT")
