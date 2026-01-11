
chaine = input("Entrez une chaîne de caractères : ")
caractere = input("Entrez un caractère à rechercher : ")

position = None
for i in range(len(chaine)):
    if chaine[i] == caractere:
        position = i
        break

if position != None:
    print(f"boucle for: Première occurrence: position {position}")
else:
    print("boucle for: Ce caractère ne figure pas dans la chaîne.")
    
    
    
    
position2 = chaine.find(caractere)
if position2 != -1:
    print(f"méthode find: Première occurrence: position {position2}")
else:
    print("méthode find: Ce caractère ne figure pas dans la chaîne.")
