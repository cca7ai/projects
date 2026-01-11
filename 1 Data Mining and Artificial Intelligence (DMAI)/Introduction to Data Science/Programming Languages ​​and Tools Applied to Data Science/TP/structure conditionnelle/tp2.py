last_name = input("Entrer votre nom : ")
first_name = input("Entrer votre prenom : ")
gender = input("Veuillez selectionner votre genre : \n 1. Masculin \n 2. Féminin \n")
if gender == "1":
    print ("Monsieur "+last_name+" "+first_name)
else:
    print ("Madame "+last_name+" "+first_name)

print("Merci, aurevoir")