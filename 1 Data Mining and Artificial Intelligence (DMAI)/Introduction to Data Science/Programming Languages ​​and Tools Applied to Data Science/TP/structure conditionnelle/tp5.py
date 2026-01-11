
x = int(input("Veuillez saisir le nombre : " ))
somme_des_diviseurs = 0
for i in range(1,x) :
    if x%i==0:
        somme_des_diviseurs = somme_des_diviseurs+i
if x==somme_des_diviseurs:
    print(x," est un nombre parfait.\n")
else:
    print(x," n'est pas un nombre parfait.\n")