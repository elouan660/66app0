import os
import random as math
from time import *
#Définition des couleurs bash
class color:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    reset = '\033[0m'
    blue = '\033[0;34m'
#titre
print(f"""{color.yellow}
  /$$$$$$   /$$$$$$                                 /$$$$$$
 /$$__  $$ /$$__  $$                               /$$$_  $$
| $$  \__/| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$ | $$$$\ $$
| $$$$$$$ | $$$$$$$  |____  $$ /$$__  $$ /$$__  $$| $$ $$ $$
| $$__  $$| $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$\ $$$$
| $$  \ $$| $$  \ $$ /$$__  $$| $$  | $$| $$  | $$| $$ \ $$$
|  $$$$$$/|  $$$$$$/|  $$$$$$$| $$$$$$$/| $$$$$$$/|  $$$$$$/
 \______/  \______/  \_______/| $$____/ | $$____/  \______/
  Version 0.3 par elouan660   | $$      | $$
        pour bash             | $$      | $$
                              |__/      |__/
 {color.reset}""")

class rtn:
    def msg(message):
        print(f"{color.yellow}System: {color.reset}{message}")
    def error(message):
        print(f"{color.red}Erreur: {message}{color.reset}")
    def iscorrect(bin):
        if bin == 1:
            print(f"{color.blue}Programme: {color.green}Correct{color.reset}")
        elif bin == 0:
            print(f"{color.blue}Programme: {color.red}Incorrect: {color.reset}{word[ale1]}")
#ouverture d'un fichier texte
system = f"{color.yellow}system> {color.reset}"
user = f"{color.green}user> {color.reset}"
rtn.msg("Voici les fichiers disponibles:")
os.system("ls")
try:
    rtn.msg("Entrez le nom du fichier")
    fileOpen = input(user)
    file = open(fileOpen, "r")
    rtn.msg(f"{fileOpen} trouvé, ouverture effectuée")
    file.close()
except FileNotFoundError:
    rtn.error(f"{fileOpen} non trouvé, souhaitez vous le créer? (y/n)")
    createData = input('>')
    if createData == "y":
        file = open(fileOpen, "x")
        file.close()
        file = open(fileOpen, "r")
        rtn.msg("fichier créé")
        file.close()
        os.system(f"nano {fileOpen}")
        rtn.msg("fichier fermé")
        exit()
    else:
        rtn.msg("fichier non créé")
        exit()

score = 0
wordcount0 = 0
wordcount1 = 0
file = open(fileOpen, "r")
list0 = file.read().split("|")
for line in list0:
    wordcount0 += 1
for line in list0:
    print('')
    word = line.split(":")
    wordcount1 = wordcount1+1
    print(f"[{wordcount1}/{wordcount0}]")
    ale0 = math.randint(0, 1)
    if ale0 == 1:
        ale1 = 0
    else:
        ale1 = 1
    rtn.msg(word[ale0])
    réponse = input(">")
    if réponse == word[ale1]:
        rtn.iscorrect(1)
        score += 1
    else:
        rtn.iscorrect(0)

if score > wordcount0/2:
    print(color.green)
else:
    print(color.red)
print(f"score: {score}/{wordcount0}")

    
     