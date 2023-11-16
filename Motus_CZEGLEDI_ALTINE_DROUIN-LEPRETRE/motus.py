import random
class Colors:
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    PURPLE = '\033[35m'
    RESET = '\033[0m'

def choose_words(lg_word):
    """
        param: lg_word
        return: word_list
        Utilisation: Choisit un mot aléatoire dans le fichier dico.txt
        """
    with open("Motus_CZEGLEDI_ALTINE_DROUIN-LEPRETRE\dico.txt", "r") as f: # Ouvre le fichier dico.txt
        word_list = f.read() # Met le contenu du fichier dans la variable reference
        word_list = word_list.split() # Transforme reference en liste
    word_list = [word for word in word_list if len(word) == lg_word]
    return word_list[random.randint(0, len(word_list)) -1]


def enter_word(lg_word):
    '''
        param: lg_word
        return: User_word
        Utilisation: Demande un mot a l'utilisateur
        '''
    User_word = input(f"{Colors.BLUE}Entrez un mot de {lg_word} lêttres : {Colors.RESET}")
    if len(User_word) != lg_word:
        while len(User_word) != lg_word:
            User_word = input(f"{Colors.BLUE}Entrez un mot de {lg_word} lêttres : {Colors.RESET}")
        return User_word.lower()
    else:
        return User_word.lower()

def init():
    '''
        param: none
        return: none
        Utilisation: Initialise le jeu
        '''
    lg = int(input(f"{Colors.ORANGE}Entrez la longueur du mot souhaitez : {Colors.RESET}"))
    actuel_word = choose_words(lg) # Choisit un mot aléatoire dans le fichier dico.txt a l'aide de la fonction dédiée
    actuel_word_noModif = actuel_word
    for i in range(len(actuel_word)):
        actuel_word = actuel_word.replace(actuel_word[i], ".") # Remplace les lettres du mot par des "."
    essais = int(input(f"{Colors.ORANGE}Entrez le nombre d'essais : {Colors.RESET}"))
    Game_Type = int(input(f"{Colors.ORANGE}Entrez le mode de jeu : \n 1 - Mode normal \n 2 - Mode super \n{Colors.RESET}")) # 1 = Mode normal, 2 = Mode super
    if Game_Type == 1: # Si le mode de jeu est "normal"
        main(actuel_word, actuel_word_noModif, essais, lg) # Lance la fonction main
    elif Game_Type == 2: # Si le mode de jeu est "super"
        super_main(actuel_word, actuel_word_noModif, essais, lg) # Lance la fonction super_main

def main(actuel_word, actuel_word_noModif, essais, lg_word):
    '''
        param: actuel_word, actuel_word_noModif, essais, lg_word
        return: none
        Utilisation: Boucle principale du jeu
        '''
    actuel_word = list(actuel_word)
    actuel_word[0] = actuel_word_noModif[0]
    actuel_word[0] = actuel_word[0].upper()
    actuel_word = "".join(actuel_word) 
    while essais != 0:
        print(f"{Colors.PURPLE}Actuellement le fragment de mot a votre disposition est : {actuel_word}{Colors.RESET}")
        mot = enter_word(lg_word) # Demande un mot a l'utilisateur a l'aide de la fonction dédiée
        for i in range(len(mot)):
            if mot[i] == actuel_word_noModif[i]: # Si la lettre est dans le mot
                actuel_word = list(actuel_word)
                actuel_word[i] = actuel_word_noModif[i]
                actuel_word[i] = actuel_word[i].upper()
                actuel_word = "".join(actuel_word)
            elif mot[i] in actuel_word_noModif: # Si la lettre est dans le mot mais pas a la bonne place
                actuel_word = list(actuel_word)
                actuel_word[i] = mot[i]
                actuel_word = "".join(actuel_word)
        essais -= 1
        
        if actuel_word.lower() == actuel_word_noModif.lower(): # Si le mot est trouvé
            print(f"{Colors.GREEN}Félicitations vous avez gagné !{Colors.RESET}")
            break
        elif essais == 0:
            print(f"{Colors.RED}Dommage, c'est perdu !'{Colors.RESET}")
            break
        print(f"{Colors.PURPLE}Il vous reste {essais} essais{Colors.RESET}")
        
def super_main(actuel_word, actuel_word_noModif, essais, lg_word):
    '''
        param: actuel_word, actuel_word_noModif, essais, lg_word
        return: none
        Utilisation: Boucle principale du jeu en mode super partie
        '''
    print(f"{Colors.PURPLE}Dans ce mode vous devrez deviner 10 mot a la suite{Colors.RESET}")
    liste_mot_deviner = [] 
    while len(liste_mot_deviner) < 10:
        if len(liste_mot_deviner) >= 1:
            lg = int(input(f"{Colors.BLUE}Entrez la longueur du mot souhaitez : {Colors.RESET}"))
            actuel_word = choose_words(lg)
            actuel_word_noModif = actuel_word
            for i in range(len(actuel_word)):
                actuel_word = actuel_word.replace(actuel_word[i], ".")
        actuel_word = list(actuel_word)
        actuel_word[0] = actuel_word_noModif[0]
        actuel_word[0] = actuel_word[0].upper()
        actuel_word = "".join(actuel_word)
        while essais != 0:
            print(f"{Colors.PURPLE}Actuellement le fragment de mot a votre disposition est : {actuel_word}{Colors.RESET}")
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
            if actuel_word.lower() == actuel_word_noModif.lower():
                print(f"{Colors.GREEN}Félicitations vous avez trouvez ce mot !{Colors.RESET}")
                liste_mot_deviner.append(actuel_word_noModif) # Ajoute le mot a la liste des mots trouvés
                break
            elif essais == 0:
                print(f"{Colors.RED}Dommage, vous n'avez pas trouvez ce mot !{Colors.RESET}")
                break
            print(f"{Colors.PURPLE}Il vous reste {essais} essais{Colors.RESET}")
        
        if essais == 0:
            print(f"{Colors.RED}Vous avez perdu la partie !{Colors.RESET}")
            print(f"{Colors.PURPLE}Les mots que vous avez trouvez sont : {liste_mot_deviner}{Colors.RESET}")
            break
        elif len(liste_mot_deviner) >= 10:
            print(f"{Colors.GREEN}Félicitations, Victoire !{Colors.RESET}")
            print(f"{Colors.PURPLE}Il vous restais {essais} essais{Colors.RESET}")
            print(f"{Colors.PURPLE}Vous avez trouvez les mots : {liste_mot_deviner}{Colors.RESET}")
        else:
            print(f"{Colors.PURPLE}Vous gagnez un bonus de 5 essais !{Colors.RESET}")
            essais += 5

init()