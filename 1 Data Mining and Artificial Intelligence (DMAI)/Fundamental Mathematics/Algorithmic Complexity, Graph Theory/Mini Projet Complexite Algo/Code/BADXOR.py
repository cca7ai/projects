# opération modulo
MODULO = 100000007

from collections import defaultdict

# lire le nombre de cas de test
nombre_de_cas = int(input())
if nombre_de_cas < 1 or nombre_de_cas > 20:
    raise ValueError("Le nombre de cas de test doit être compris entre 1 et 20.")

# pour chaque cas de test, car tout ce bloc de code est un cas de test
for numero_cas in range(1, nombre_de_cas + 1):
    # lire N (taille de A) et M (taille de B) séparé par des espaces
    taille_A, taille_B = map(int, input().split())

    # Lecture des tableaux A et B dont les éléments de chacun sont séparés par des espaces,
    # ensuite, chaque élément de chaque tableau est converti en entier par (map(int,) et le tableau est stoqué sous forme de liste
    tableau_A = list(map(int, input().split())) if taille_A > 0 else []
    tableau_B = list(map(int, input().split())) if taille_B > 0 else []  
             
    # Vérification que les éléments de A et B sont compris entre 0 et 1000
    for a in tableau_A: 
        if a < 0 or a > 1000:
            raise ValueError("Les éléments de A doivent être compris entre 0 et 1000.")
    for b in tableau_B:
        if b < 0 or b > 1000:
            raise ValueError("Les éléments de B doivent être compris entre 0 et 1000.")
     
  
    dp = defaultdict(int) # Pour stocquer le nombre de sous-ensemble ayant un xor donné, Utilisation de defaultdict pour éviter les KeyError
    dp[0] = 1  # Le sous-ensemble vide a un XOR de 0
    B = set(tableau_B)

    for a in tableau_A:
        nouveau_dp = dp.copy()
        for xor_actuel, count in dp.items():
            if count: # nombre de sous-ens ayant un XOR actuel existant
                nouveau_xor = xor_actuel ^ a 
                nouveau_dp[nouveau_xor] = (nouveau_dp.get(nouveau_xor, 0) + count) % MODULO
        dp = nouveau_dp
        
        total = 0
        for xor_value, count in dp.items():
            if xor_value not in B:
                total = (total + count) % MODULO

        # Affichage du résultat
    print(f"Case {numero_cas}: {total}")