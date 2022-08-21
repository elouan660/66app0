from tkinter import *
from time import *
#Tests Tkinter
#Apparence fenetre
fenetre = Tk()
fenetre.call('wm', 'iconphoto', fenetre._w, PhotoImage(file='images/icon.gif'))
fenetre.title("66app0 tkinter 0.0")
fenetre.geometry("1080x720")
fenetre.minsize(480, 360)
fenetre.config(background='#993a2d')
#Contenu fenetre
frame = Frame(fenetre, bg='#993a2d')

label_title = Label(frame, text="Hello world", font=("Arial", 40), bg='#993a2d', fg='#ffffff')
label_title.pack(expand=YES)

label_subtitle = Entry(frame, font=("Arial", 26), bg='#993a2d', fg='#ffffff')
label_subtitle.pack(expand=YES)

frame.pack(expand=YES)
fenetre.mainloop()
#Définition des couleurs bash
class color:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    reset = '\033[0m'
    blue = '\033[0;34m'
#test
def color(message):

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
  1er test de tkinter         | $$      | $$
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
            rtn.msg("veuillez entrer 'clear' après la fin du programme")
            fail = 1
            break
    if fail == 0:
        print('')
        rtn.msg("Félicitation, c'est un sans faute")
        rtn.score()
except FileNotFoundError:
    print()
