somme_argent = 100000
liste_depenses = [25000,12500,38000,9000,45000,1000]
toutes_les_depenses = 0

for x in liste_depenses:
    toutes_les_depenses += x

somme_depenses = 0
while somme_argent >= somme_depenses:
    for depense in liste_depenses:
        somme_depenses += depense
        
print("Montant inssuffisant")

supplement = toutes_les_depenses - somme_argent

print("Le supplément pour couvrir toutes les dépenses est : ", supplement)
