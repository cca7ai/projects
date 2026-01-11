x = int(input("Veuillez saisir un nombre : "))
factoriel_x = 1
if x==0 or x==1:
    print ("Factoriel de ",x," = 1")
else:
    for i in range(1,x+1):
        factoriel_x = factoriel_x *i
    print("Factoriel de ",x," = ",factoriel_x)