import json
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Sélection de la base de données et de la collection
db = client["minigmaps"]
collection = db["lieux"]

# Charger les données depuis le fichier JSON
input_file = "lieux.json"
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Insérer les nouvelles données
collection.insert_many(data)

print(f" {len(data)} lieux ont été importés dans la collection 'lieux' de la base 'minigmaps'.")
