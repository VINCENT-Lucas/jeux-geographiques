import pyautogui, keyboard, requests, time, random
from bs4 import BeautifulSoup
import easyocr

'''
V1, meilleur score: 103 667
'''


def lire_monument(reader):
    text_ = reader.readtext('screenshot.png')
    print('\n', text_)
    if len(text_) >= 1:
        return text_[0][1]
    return "None"

def press_start():
    pyautogui.click(x=950, y=855)

def take_screenshot():
    pyautogui.screenshot("screenshot.png", region=(320, 10, 1000, 70))

def save_data(dictionnaire, nomFichier):
    with open(nomFichier, 'w', encoding='utf-8') as f:
        for clé, valeur in dictionnaire.items():
            f.write(f"{clé}@ {valeur}\n")

def load_data(nomFichier):
    dictionnaire = {}
    try:
        with open(nomFichier, 'r', encoding='utf-8') as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne:  # Ignorer les lignes vides
                    clé, valeur = ligne.split('@', 1)  # Séparer la clé et la valeur
                    dictionnaire[clé.strip()] = valeur.strip()  # Supprimer les espaces autour
    except FileNotFoundError:
        with open(nomFichier, 'w', encoding='utf-8') as f:
            pass
        print(f"Le fichier {nomFichier} n'a pas été trouvé. Il a été créé")
    except Exception as e:
        print(f"Une erreur est survenue lors de la lecture du fichier : {e}")
    return dictionnaire

def wait(key:'str'):
    while not keyboard.is_pressed(key):
        pass

def play(data, reader):
    wait("a")
    # Press start
    press_start()
    # On répète 20 fois
    while not keyboard.is_pressed("q"):
        wait("a")
        # On lit le nom du monument
        take_screenshot()
        nom_monument = lire_monument(reader)
        coords = None
        for key in data:
            if key[:30] == nom_monument[:30]:
                coords = eval(data[key])
                print(f"COO: {coords}")
        if coords is None:
            print(f"{nom_monument} ***NOUVEAU***")
        # On récupère les coordonnées associées
        else:
            print(coords[0], coords[1])
            pyautogui.click(coords[0], coords[1])

if __name__ == "__main__":
    reader = easyocr.Reader(['en'], gpu=False)
    data = load_data("data.txt")
    play(data, reader)