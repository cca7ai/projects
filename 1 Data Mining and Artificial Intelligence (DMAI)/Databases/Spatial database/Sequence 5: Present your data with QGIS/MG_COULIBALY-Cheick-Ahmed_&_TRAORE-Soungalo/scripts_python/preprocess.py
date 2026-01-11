import json

# Charger le fichier source
input_file = "adresses_enregistrees.json"
output_file = "lieux.json"

# Structure des horaires par défaut
default_hours = [
    {"jour": "Lundi", "heures": "00:00-00:00"},
    {"jour": "Mardi", "heures": "00:00-00:00"},
    {"jour": "Mercredi", "heures": "00:00-00:00"},
    {"jour": "Jeudi", "heures": "00:00-00:00"},
    {"jour": "Vendredi", "heures": "00:00-00:00"},
    {"jour": "Samedi", "heures": "00:00-00:00"},
    {"jour": "Dimanche", "heures": "00:00-00:00"}
]

# Lire le fichier JSON
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Transformation des données
lieux_transformes = []
for feature in data["features"]:
    props = feature["properties"]
    location = props.get("location", {})

    lieu = {
        "nom": location.get("name", "Inconnu"),
        "type": "Inconnu",  # Type par defaut, puis modifié manuellement pour chaque lieu pour correspondre au type exacte
        "horaires": default_hours,
        "source": "Gmaps",
        "geometry": feature["geometry"],
        "ville": location.get("address", "Burkina Faso").split(",")[-1].strip()
    }

    lieux_transformes.append(lieu)

# Écrire le fichier de sortie
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(lieux_transformes, f, indent=4, ensure_ascii=False)

print(f"Fichier converti enregistré sous {output_file}")

