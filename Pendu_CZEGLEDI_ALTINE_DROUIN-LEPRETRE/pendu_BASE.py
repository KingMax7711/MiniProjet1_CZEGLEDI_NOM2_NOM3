from random import randint # Importe la fonction randint du module random


def demander_lettre():
    """
        param: none
        return: lettre
        Utilisation: Demande une lettre à l'utilisateur et vérifie qu'elle est valide"""
    
    lettre_valid = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x", "y", "z"]
    lettre = input("Entrez une lettre : ")
    lettre = lettre.lower() # Met la lettre en minuscule
    while lettre not in lettre_valid: # Boucle tant que la lettre n'est pas valide
        lettre = input("Entrez une lettre : ")
    return lettre

def remplace(reference, actuel, lettre):
    """
        param: reference, actuel, lettre
        return: actuel
        Utilisation: Remplace les "_" par la lettre si elle est dans le mot"""

    if lettre in reference: 
        actuel = list(actuel) # Transforme actuel en liste pour pouvoir remplacer les "_" par la lettre
        for i in range(len(reference)):
            if reference[i] == lettre:
                actuel[i] = lettre # Remplace les "_" par la lettre
        actuel = "".join(actuel) # Transforme actuel en string
        return actuel
    else:
        print("La lettre n'est pas dans le mot")
        return actuel

def init():
    """
        param: none
        return: none
        Utilisation: Initialise le jeu"""
    reference = ["Kayak", "Pomme", "Banane", "Piscine"]
    reference = reference[randint(0, len(reference))] # Prend un mot au hasard dans la liste
    actuel = ""
    essais = int(input("Entrez le nombre d'essais : "))
    for i in range(len(reference)):
        actuel += "_" # Met autant de "_" que de lettres dans le mot
    lettre_jouees = ""
    main(reference, actuel, essais, lettre_jouees)
    

def main(reference, actuel, essais, lettre_jouees):
    """
        param: reference, actuel, essais, lettre_jouees
        return: none
        Utilisation: Boucle principale du jeu"""
    
    while essais > 0:
        print("\033[0;94mIl vous reste {} essais\033[0m".format(essais))
        print("\033[0;94mActuellement vous avez trouvé : {}\033[0m".format(actuel))
        print("\033[0;94mVous avez déja utilisé les lêttres : {}\033[0m".format(lettre_jouees))
        lettre = demander_lettre() # Demande une lettre à l'utilisateur a l'aide la fonction déiée
        lettre_jouees += lettre 
        
        oldActuel = actuel
        actuel = remplace(reference, actuel, lettre) # Remplace les "_" par la lettre si elle est dans le mot a l'aide de la fonction dédiée


        if oldActuel == actuel:
            essais -= 1
            oldactuel = actuel
        else:
            oldActuel = actuel
            
        if "_" not in actuel: # Si il n'y a plus de "_" dans le mot, l'utilisateur a gagné
            print("\033[0;92mVous avez gagné, le mot était {}\033[0m".format(reference))
            break
        if essais == 0: # Si il n'y a plus d'essais, l'utilisateur a perdu
            print("\033[0;91mVous avez perdu, le mot était {}\033[0m".format(reference))
            break

init()

