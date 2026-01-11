import json
import csv

# Fichiers d'entrée et sortie
input_file = "lieux.json"  
output_file = "lieux.csv"  

# Dictionnaire des villes associées aux régions
ville_region = {
    "Ouagadougou": "Centre",
    "Bobo-Dioulasso": "Hauts-Bassins",
    "Koudougou": "Centre-Ouest",
    "Dori": "Sahel",
    "Fada N’Gourma": "Est",
    "Tenkodogo": "Centre-Est",
    "Banfora": "Cascades",
    "Gaoua": "Sud-Ouest",
    "Ziniaré": "Plateau-Central",
    "Kaya": "Centre-Nord",
    "Manga": "Centre-Sud",
    "Ouahigouya": "Nord",
    "Dédougou": "Boucle du Mouhoun"
}

# Charger les lieux depuis le JSON
with open(input_file, "r", encoding="utf-8") as f:
    lieux = json.load(f)

# Écriture dans le fichier CSV
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    
    # En-tête du fichier CSV
    writer.writerow(["nom", "type", "ville", "region", "latitude", "longitude"])

    for lieu in lieux:
        nom = lieu["nom"]
        type_lieu = lieu["type"]
        ville = lieu["ville"]
        region = ville_region.get(ville, "Inconnue")  # Associer la ville à sa région
        latitude, longitude = lieu["geometry"]["coordinates"][1], lieu["geometry"]["coordinates"][0]
        
        #  Écrire la ligne dans le CSV
        writer.writerow([nom, type_lieu, ville, region, latitude, longitude])

print(f" Fichier CSV généré : {output_file}")

