import pyautogui
from PIL import Image


def find_target(target_color = (232, 59, 52)):
    # TARGET: #FFFFFF #E83B34
    #         #FFFFFF #EF3B37

    img = Image.open("aaaaaa.png").convert("RGB")
    width, height = img.size
    for x in range(width):
        for y in range(height):
            pixel_color = img.getpixel((x, y))
            print(pixel_color)
            if pixel_color == target_color:
                print("PREMIER PIXEL TROUVE")
                if img.getpixel((x-1, y))==img.getpixel((x-1, y+1))=='#FFFFFF' and img.getpixel((x, y+1))=='#EF3B37':
                    return x, y
    print("RIEN TROUVE")
    return None

def est_rouge(couleur):
    if 230 < couleur[0] and couleur[1] < 200 and couleur[2] < 200:
        return True
    return False

def est_blanc(couleur):
    if 230 < couleur[0]and 230 < couleur[1]  and 230 < couleur[2]:
        return True
    return False

def explorer():
    target_color = (232, 59, 52)
    img = Image.open("aaaaaa.png").convert("RGB")
    width, height = img.size
    for x in range(width):
        for y in range(height):
            
            pixel_color = img.getpixel((x, y))
            print(f"({x}, {y}): {pixel_color}")
            if est_rouge(pixel_color) :
                print(f"PREMIER PIXEL TROUVE en {x}, {y}")
                print(img.getpixel((x, y)))
                print(f"gauche {img.getpixel((x-1, y))}, droite {img.getpixel((x+1, y))}, haut {img.getpixel((x, y-1))}, bas {img.getpixel((x, y+1))}")
                if est_blanc(img.getpixel((x-1, y))):
                    print(f"--------------DETECTE en {x}, {y}")
                    print(img.getpixel((x-1, y)))

explorer()

