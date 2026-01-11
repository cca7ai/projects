import random

def generateur_phrase():
    phrase = input("Veuillez entrer une chaine de la forme suivante : mot1/mot2/mot3/mot4 :")
    liste_mots = phrase.strip('/').split('/')
    random.shuffle(liste_mots)
    if len(liste_mots) <10 :
        print("Les deux premiers mots sont : ", liste_mots[:2])
    else:
        print("Les trois derniers mots sont : ", liste_mots[-3:])

generateur_phrase()