import json
import math
from pymongo import MongoClient
from datetime import datetime

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["minigmaps"]
collection = db["lieux"]

# Fonction pour calculer la distance entre deux points (Haversine Formula)
def calculer_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon de la Terre en km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c  # Distance en km

# Vérifier si un lieu est ouvert à une date et une heure données
def est_ouvert(lieu, date_heure):
    jour_semaine = date_heure.strftime("%A")  # Ex: "Thursday"
    jours_traduits = {
        "Monday": "Lundi", "Tuesday": "Mardi", "Wednesday": "Mercredi",
        "Thursday": "Jeudi", "Friday": "Vendredi", "Saturday": "Samedi", "Sunday": "Dimanche"
    }
    jour_recherche = jours_traduits[jour_semaine]  # Ex: "Jeudi"
    heure_recherche = date_heure.strftime("%H:%M")  # Ex: "12:00"

    # Vérifier les horaires du jour recherché
    for jour in lieu["horaires"]:
        if jour["jour"] == jour_recherche:
            if jour["heures"] == "Fermé":
                return False
            elif jour["heures"] == "00:00-00:00":  # Lieu ouvert 24h/24
                return True
            elif isinstance(jour["heures"], list):  # Cas de plusieurs plages horaires
                for plage in jour["heures"]:
                    debut, fin = plage.split("–")
                    if debut <= heure_recherche <= fin or (debut > fin and (heure_recherche >= debut or heure_recherche <= fin)):
                        return True
            else:  # Cas d'un seul horaire
                debut, fin = jour["heures"].split("-")
                if debut <= heure_recherche <= fin or (debut > fin and (heure_recherche >= debut or heure_recherche <= fin)):
                    return True

    return False  # Si aucune plage horaire ne correspond


# Fonction principale pour rechercher les lieux
def rechercher_lieux(s, t, lon, lat):
    date_heure = datetime.strptime(t, "%Y-%m-%d %H:%M")  # Convertir la date en objet datetime

    # Rechercher les lieux filtrés par nom ou type
    query = {"$or": [{"nom": {"$regex": s, "$options": "i"}}, {"type": {"$regex": s, "$options": "i"}}]}
    lieux = list(collection.find(query))

    # Calculer la distance et filtrer selon l'ouverture
    resultats = []
    for lieu in lieux:
        lieu_lat, lieu_lon = lieu["geometry"]["coordinates"][1], lieu["geometry"]["coordinates"][0]
        distance = calculer_distance(lat, lon, lieu_lat, lieu_lon)
        ouvert = est_ouvert(lieu, date_heure)

        resultats.append({
            "nom": lieu["nom"],
            "ville": lieu["ville"],
            "coordonnees": {"longitude": lieu_lon, "latitude": lieu_lat},
            "disponibilite": "Ouvert" if ouvert else "Fermé"
        })

    # Trier les résultats par distance
    resultats = sorted(resultats, key=lambda x: calculer_distance(lat, lon, x["coordonnees"]["latitude"], x["coordonnees"]["longitude"]))

    return resultats

# Utilisation
if __name__ == "__main__":
    s = "musée"  # Recherche des musées
    t = "2025-03-20 12:00"  # Date et heure de recherche
    lon, lat = -1.5197, 12.3714  # Position (ex: Ouagadougou)

    lieux_proches = rechercher_lieux(s, t, lon, lat)

    # Afficher les résultats de manière simple et lisible
    print(json.dumps(lieux_proches, indent=4, ensure_ascii=False))
