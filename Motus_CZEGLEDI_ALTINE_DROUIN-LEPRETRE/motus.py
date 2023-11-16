import random

def choose_words(lg_word):
    with open("Motus_CZEGLEDI_ALTINE_DROUIN-LEPRETRE\dico.txt", "r") as f: # Ouvre le fichier dico.txt
        word_list = f.read() # Met le contenu du fichier dans la variable reference
        word_list = word_list.split() # Transforme reference en liste
    word_list = [word for word in word_list if len(word) == lg_word]
    return word_list[random.randint(0, len(word_list)) -1]


def enter_word(lg_word):
    User_word = input("Entrez un mot de {} lêttres : ".format(lg_word))
    if len(User_word) != lg_word:
        while len(User_word) != lg_word:
            User_word = input("Entrez un mot de {} lêttres : ".format(lg_word))
        return User_word.lower()
    else:
        return User_word.lower()

def init():
    lg = int(input("Entrez la longueur du mot souhaitez : "))
    actuel_word = choose_words(lg)
    actuel_word_noModif = actuel_word
    for i in range(len(actuel_word)):
        actuel_word = actuel_word.replace(actuel_word[i], ".")
    essais = int(input("Entrez le nombre d'essais : "))
    Game_Type = int(input("Entrez le mode de jeu : \n 1 - Mode normal \n 2 - Mode super \n"))
    if Game_Type == 1:
        main(actuel_word, actuel_word_noModif, essais, lg)
    elif Game_Type == 2:
        super_main(actuel_word, actuel_word_noModif, essais, lg)

def main(actuel_word, actuel_word_noModif, essais, lg_word):
    actuel_word = list(actuel_word)
    actuel_word[0] = actuel_word_noModif[0]
    actuel_word[0] = actuel_word[0].upper()
    actuel_word = "".join(actuel_word)
    while essais != 0:
        print("Actuellement le fragment de mot a votre disposition est : {}".format(actuel_word))
        mot = enter_word(lg_word)
        for i in range(len(mot)):
            if mot[i] == actuel_word_noModif[i]:
                actuel_word = list(actuel_word)
                actuel_word[i] = actuel_word_noModif[i]
                actuel_word[i] = actuel_word[i].upper()
                actuel_word = "".join(actuel_word)
            elif mot[i] in actuel_word_noModif:
                actuel_word = list(actuel_word)
                actuel_word[i] = mot[i]
                actuel_word = "".join(actuel_word)
        essais -= 1
        
        if actuel_word.lower() == actuel_word_noModif.lower():
            print("Félicitations vous avez gagné !")
            break
        elif essais == 0:
            print("Dommage, c'est perdu !")
            break
        print("Il vous reste {} essais".format(essais))
        
def super_main(actuel_word, actuel_word_noModif, essais, lg_word): 
    print("Dans ce mode vous devrez deviner 10 mot a la suite")
    liste_mot_deviner = [] 
    while len(liste_mot_deviner) < 10:
        print("DEBUG Liste Mot deviner : {}".format(liste_mot_deviner))
        if len(liste_mot_deviner) >= 1:
            lg = int(input("Entrez la longueur du mot souhaitez : "))
            actuel_word = choose_words(lg)
            actuel_word_noModif = actuel_word
            for i in range(len(actuel_word)):
                actuel_word = actuel_word.replace(actuel_word[i], ".")
        actuel_word = list(actuel_word)
        actuel_word[0] = actuel_word_noModif[0]
        actuel_word[0] = actuel_word[0].upper()
        actuel_word = "".join(actuel_word)
        while essais != 0:
            print("Actuellement le fragment de mot a votre disposition est : {}".format(actuel_word))
            if len(liste_mot_deviner) >= 1:
                mot = enter_word(lg)
            else:
                mot = enter_word(lg_word)
            for i in range(len(mot)):
                if mot[i] == actuel_word_noModif[i]:
                    actuel_word = list(actuel_word)
                    actuel_word[i] = actuel_word_noModif[i]
                    actuel_word[i] = actuel_word[i].upper()
                    actuel_word = "".join(actuel_word)
                elif mot[i] in actuel_word_noModif:
                    actuel_word = list(actuel_word)
                    actuel_word[i] = mot[i]
                    actuel_word = "".join(actuel_word)
            essais -= 1
            print("DEBUG: {}".format(actuel_word_noModif))
            print("DEBUG: {}".format(actuel_word))
            if actuel_word.lower() == actuel_word_noModif.lower():
                print("Félicitations vous avez trouvez ce mot !")
                liste_mot_deviner.append(actuel_word_noModif)
                break
            elif essais == 0:
                print("Dommage, vous n'avez pas trouvez ce mot !")
                break
            print("Il vous reste {} essais".format(essais))
        
        if essais == 0:
            print("Vous avez perdu la partie !")
            print("Les mots que vous avez trouvez sont : {}".format(liste_mot_deviner))
            break
        elif len(liste_mot_deviner) >= 10:
            print("Félicitations, Victoire !")
            print("Il vous restais {} essais".format(essais))
            print("Vous avez trouvez les mots : {}".format(liste_mot_deviner))
        else:
            print("Vous gagnez un bonus de 5 essais !")
            essais += 5

        

init()