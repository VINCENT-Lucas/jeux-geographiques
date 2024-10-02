# Bot sur jeux-geographiques

En jouant à un quizz de géographie sur le site https://www.jeux-geographiques.com/ on s'est rendu compte de plusieurs scores poarticulièrement douteux.
On s'est donc lancé dans la création d'un bot afin de regarder quels scores étaient atteignables.

Langages utilisés: Python
Librairies utilisées: pyautogui, keyboard, easyocr

# Fonctionnement du bot 

Pour lancer l'apprentissage d'un bot sur un quizz en particulier, il faut passer le quizz en plein écran (nécessaire pour calibrer les endroits où cliquer), puis appuyer sur la touche "A" pour lancer l'apprentissage.

Une fois la touche "A" appuyée, le bot va scanner le nom du quizz, et générer un fichier texte (qui servira de base de données) pour ce quizz s'il n'existe pas, ou charger les données s'il existe.

![Détection du quizz](assets/TitleDetection.png)
