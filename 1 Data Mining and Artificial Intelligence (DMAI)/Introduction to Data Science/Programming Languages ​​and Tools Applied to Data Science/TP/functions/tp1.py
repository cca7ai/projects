def nombreDivisibles():
    liste_nombre = [42,48,5,3,7,6,8]
    entier_n = 4
    multiples_n = []
    for x in liste_nombre:
        if x%entier_n==0:
            multiples_n.append(x)
    print(len(multiples_n), "élement(s) de cette liste est divisible par ",entier_n)

nombreDivisibles()