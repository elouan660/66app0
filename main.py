import os
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
  Version 0.2 par elouan660   | $$      | $$
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
            print(f"{color.blue}Programme: {color.red}Incorrect: {color.reset}{word[wordcount]}")
    def score():
        if wordcount//2 < tempo:
            print(f"{color.yellow}Score: {color.red}{wordcount//2}/{tempo}{color.reset}")
        else:
            print(f"{color.yellow}Score: {color.green}{wordcount//2}/{tempo}{color.reset}")

#ouverture d'un fichier texte
system = f"{color.yellow}system> {color.reset}"
user = f"{color.green}user> {color.reset}"
rtn.msg("Voici les fichiers disponibles:")
os.system("ls")
try:
    rtn.msg("Entrez le nom du fichier")
    fileOpen = input(user)
    file = open(fileOpen, "r")
    rtn.msg(fileOpen + " trouvé, ouverture effectuée")
    file.close()
except FileNotFoundError:
    rtn.error(fileOpen + " non trouvé, souhaitez vous le créer? (y/n)")
    createData = input('>')
    if createData == "y":
        file = open(fileOpen, "x")
        file.close()
        file = open(fileOpen, "r")
        rtn.msg("fichier vide créé")
        file.close()
        rtn.msg("fichier fermé")
        exit()
    else:
        rtn.msg("fichier non créé")
        exit()

#Apprentissage
fail = 0
swap = input("voulez vous activer le mode inversé? (y/n)")
if swap == 'y':
    swap = 1
else:
    swap = 0

try:
    file = open(fileOpen, "r")
    rtn.msg("Programme lancé")
    list = file.read()
    word = list.split(":")
    wordcount = 0
    print('')
    tempo = 0
    fail = 0
    for ligne in word:
        tempo += 1
    tempo //= 2
    for x in range(tempo):
        print(word[wordcount])
        réponse = input(">")
        wordcount += 1
        if word[wordcount] == réponse:
            rtn.iscorrect(1)
            wordcount += 1
        else:
            rtn.iscorrect(0)
            print('')
            rtn.score()
        fail = 1
        break
    if fail == 0:
        print('')
        rtn.msg("Félicitation, c'est un sans faute")
        rtn.score()
    rtn.msg("Entrez c pour clear, entrez autre chose sinon")
    clear = input(user)
    if clear == "c":
        os.system("clear")
except FileNotFoundError:
    print()
