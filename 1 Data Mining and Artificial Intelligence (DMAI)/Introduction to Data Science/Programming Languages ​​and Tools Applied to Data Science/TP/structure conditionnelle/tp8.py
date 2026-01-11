chaine = input("Entrez une chaîne de caractères : ")

chaine_normalisee = chaine.replace(" ", "").lower()

if chaine_normalisee == chaine_normalisee[::-1]:  # Comparaison avec la chaîne inversée
    print(f"La chaîne '{chaine}' est un palindrome.")
else:
    print(f"La chaîne '{chaine}' n'est pas un palindrome.")
        