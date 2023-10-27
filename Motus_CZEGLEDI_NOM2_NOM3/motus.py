import random

def choose_words():
    word_list = ['girafes', 'plonger', 'chapeau']
    return word_list[random.randint(0, len(word_list)) -1]


def enter_word():
    User_word = input("Entrez un mot de 7 lêttres : ")
    if len(User_word) != 7:
        while len(User_word) != 7:
            User_word = input("Entrez un mot de 7 lêttres : ")
        return User_word.lower()
    else:
        return User_word.lower()

def init():
    actuel_word = choose_words()
    actuel_word_noModif = actuel_word
    for i in range(len(actuel_word)):
        actuel_word = actuel_word.replace(actuel_word[i], ".")
    essais = int(input("Entrez le nombre d'essais : "))
    main(actuel_word, actuel_word_noModif, essais)

def main(actuel_word, actuel_word_noModif, essais):
    actuel_word = list(actuel_word)
    actuel_word[0] = actuel_word_noModif[0]
    actuel_word[0] = actuel_word[0].upper()
    actuel_word = "".join(actuel_word)
    while essais != 0:
        print("Actuellement le fragment de mot a votre disposition est : {}".format(actuel_word))
        mot = enter_word()
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
        
        if actuel_word == actuel_word_noModif:
            print("Félicitations vous avez gagné !")
            break
        elif essais == 0:
            print("Dommage, c'est perdu !")
            break
        print("Il vous reste {} essais".format(essais))
        
init()