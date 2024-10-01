from GeoPlayerV1 import *
print("DEBUT DE L'ENTRAINEMENT")

DETECT_HIGH_PIXEL = (1725, 145)
DETECT_LOW_PIXEL = (1725, 200)

def detect(name: str, data):
    for elem in data.keys():
        if name[:25] == elem[:25]:
            return True

reader = easyocr.Reader(['en'], gpu=False)

def get_quizz_name():
    pyautogui.screenshot("quizzName.png", region=(350, 250, 1200, 400))
    text_ = reader.readtext('quizzName.png')
    print('\n', text_)
    if len(text_) >= 1:
        print(text_)
        #return text_[1][1] + '.txt'
        return '_'.join([element[1] for element in text_[1:]]) + '.txt'
    return 'dataTraining.txt'

def start_training(quizzname=None):
    wait('a')
    if quizzname is None:
        quizzname = get_quizz_name()
    data = load_data('data/' + quizzname)
    press_start()
    while not keyboard.is_pressed('q'):
        # On attend que le nom soit apparu
        wait_before_guess()
        take_screenshot()
        nom_monument = lire_monument(reader)
        if nom_monument != "None":
            
            if nom_monument not in data:
                # On trouve de nouvelles données. On clique au hasard, puis on récupère les données
                pyautogui.click(253, 139)
                print(f"{nom_monument} ***NOUVEAU***")
                time.sleep(0.75)
                pos = find_target()
                if pos is not None:
                    print("DATA AJOUTEES")
                    data[nom_monument] = (pos[0], pos[1])
                    print(f"NOUVELLES DONNEES: {nom_monument, (pos[0], pos[1])}")
            else:
                print("-------TAG-------")
                coords = data[nom_monument]
                if type(coords)==str:
                    coords = eval(coords)
                print(f"Click en {coords[0]}, {coords[1]}")
                pyautogui.click(coords[0]+3, coords[1]+7)
            wait_before_new_question()

    save_data(data, 'data/' + quizzname)
    print(data, 'saved in', quizzname)
    print("FIN DE L'ENTRAINEMENT")

def est_rouge(couleur):
    if 230 < couleur[0] and couleur[1] < 200 and couleur[2] < 200:
        return True
    return False

def est_blanc(couleur):
    if 230 < couleur[0]and 230 < couleur[1]  and 230 < couleur[2]:
        return True
    return False

def find_target():
    screenshot = pyautogui.screenshot("aaaaaa.png")
    img = screenshot.convert("RGB")
    width, height = img.size
    for x in range(width):
        for y in range(height):
            pixel_color = img.getpixel((x, y))
            if est_rouge(pixel_color) :
                if est_blanc(img.getpixel((x-1, y))):
                    return (x,y)
    return None

def wait_before_guess():
    while not keyboard.is_pressed('q'):
        screenshot = pyautogui.screenshot()
        img = screenshot.convert("RGB")
        if img.getpixel(DETECT_LOW_PIXEL) == (51, 255, 51) and img.getpixel(DETECT_HIGH_PIXEL) == (255, 255, 255):
            return

def wait_before_new_question():
    while not keyboard.is_pressed('q'):
        screenshot = pyautogui.screenshot()
        img = screenshot.convert("RGB")
        if detect_end():
            replay()
            return
        if img.getpixel((1725, 250)) == (51, 255, 51) and img.getpixel((1725, 170)) == (51, 255, 51):
            return

def detect_end():
    print('---ENTREE DETECT END')
    end_color = (226, 249, 255)
    screenshot = pyautogui.screenshot()
    img = screenshot.convert("RGB")
    if img.getpixel((726, 141)) == end_color and img.getpixel((1165, 140)) == end_color and img.getpixel((731, 884)) == end_color and img.getpixel((1179, 878)) == end_color:
        print('---DETECTEE')
        return True
    return False

def replay():
    pyautogui.press('f5')
    time.sleep(1)
    pyautogui.moveTo(876, 479)
    pyautogui.scroll(15000)
    time.sleep(1)
    pyautogui.scroll(-900)
    time.sleep(1)
    pyautogui.click((949, 643))
    time.sleep(2)
    press_start()

# L'idée générale est d'obtenir le nom du quizz: Dans le html ?
# -----> get_quizz_name()

# En suite, en fonction du nom du quizz, on charge les data d'un fichier portant le nom du quizz.
# S'il existe pas, on le crée.

# On joue au quizz en boucle.
# Normalement, on appuie toujours au même endroit pour start
# Attention, le nombre de trucs à guess change.

# ---------- Phase de train --------
# On regarde si on a la cible en base de données
# Si on l'a, on ping
# Sinon, on ping au hasard et on scanne pour la couleur rouge de la solution, on stocke les données associées

start_training()