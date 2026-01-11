import csv
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qgis.core import *
from qgis.utils import iface

# Sélectionner les couches
active_layer = iface.activeLayer()  # Couche des régions
statistics_layer = QgsProject.instance().mapLayersByName("statistics")  # Couche des restaurants


if not active_layer or not statistics_layer:
    print("Veuillez sélectionner la couche des régions et vérifier la présence de 'statistics'.")
    exit()
else:
    statistics_layer = statistics_layer[0]  # Prendre la première couche trouvée

    # Initialisation de l'outil de mesure des superficies
    d = QgsDistanceArea()
    d.setEllipsoid('WGS84')

    # Dictionnaire contenant le nombre de restaurants par région
    nb_restaurants = {}

    # Lire les données de la couche statistics
    for f in statistics_layer.getFeatures():
        region_name = f["region"]
        count = f["count"]
        nb_restaurants[region_name] = count

    # Liste des données des régions
    regions_data = []

    for f in active_layer.getFeatures():
        region_name = f["ADM1_FR"]

        if region_name in nb_restaurants:  # Vérification que la région existe dans statistics
            superficie = d.measureArea(f.geometry()) / 1e6  # Conversion en km²
            densite = nb_restaurants[region_name] / superficie  # Densité

            regions_data.append((region_name, nb_restaurants[region_name], superficie, densite))

    # Trier les régions par densité décroissante
    regions_data.sort(key=lambda x: x[3], reverse=True)

    # Fichier CSV de sortie (dans le dossier projet_&_plans_QGIS)
    output_csv = "densite_restaurants.csv"

    # Écriture des données dans le fichier CSV
    with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Région", "Nombre de restaurants", "Superficie (km²)", "Densité (restaurants/km²)"])

        for region, nb_restos, superficie, densite in regions_data:
            writer.writerow([region, nb_restos, f"{superficie:.2f}", f"{densite:.6f}"])

    print(f"\n Données exportées avec succès dans {output_csv} !")
