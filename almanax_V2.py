import urllib.request
import re
import datetime
import os

#Pour la fenêtre
from tkinter import *

def better_reading(content):
    content[0] = content[0].replace("\\xc3\\xa9", "é")
    content[0] = content[0].replace("\\xc3\\xa0", "à")
    content[0] = content[0].replace("\\xc3\\xa8", "è")
    content[0] = content[0].replace("\\xc3\\xa7", "ç")
    content[0] = content[0].replace("\\'", "'")
    content[0] = content[0].replace("\\n", "")

def get_ressource():
    page = urllib.request.urlopen("https://www.krosmoz.com/fr/almanax")
    content = re.findall('<p class="fleft">(.+?)</p>', str(page.read()))
    better_reading(content)
    return content[0]

def get_bonus():
    page = urllib.request.urlopen("https://www.krosmoz.com/fr/almanax")
    content = re.findall('<div class="more">(.+?)</div>', str(page.read()))
    content[0] = content[0].replace("<b>", "")
    content[0] = content[0].replace("</b>", "")
    content[0] = content[0].split(".")[0]
    better_reading(content)
    return content[0]

# On veut créer une nouvelle fonction qui récupère l'image de la ressource de l'almanax et la stocke dans une variable pour pouvoir l'afficher dans la fenêtre plus tard

def get_image():
    page = urllib.request.urlopen("https://www.krosmoz.com/fr/almanax")
    # L'image se trouve dans la balise <img src="..."> dans la balise <div class="more-infos-content">
    # On veut donc récupérer le nom de l'image en .png pour la stocker dans la variable img
    img = re.findall('<div class="more-infos-content">.+<img src="(.+?)">', str(page.read()))
    
# Création de la fenêtre dans laquelle on affiche le resultat de la fonction get_ressource() et get_bonus()

window = Tk()
window.title("Almanax")
window.geometry("1400x200")
window.minsize(200, 200)
window.maxsize(1400, 1400)
window.config(background='#41B77F')

# Création d'un label pour afficher le résultat de la fonction get_ressource()

label_ressource = Label(window, text=get_ressource(), font=("Courrier", 20), bg='#41B77F', fg='white')
label_ressource.pack()

# Création d'un label pour afficher le résultat de la fonction get_bonus()

label_bonus = Label(window, text=get_bonus(), font=("Courrier", 20), bg='#41B77F', fg='white')
label_bonus.pack()

# Affichage de l'image

window.mainloop()