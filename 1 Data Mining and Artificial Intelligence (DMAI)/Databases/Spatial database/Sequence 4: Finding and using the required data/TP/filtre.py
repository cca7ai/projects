import json
from geopy.distance import geodesic

# Coordonnées du Siège du SIAO
siao_coords = (12.350117365258793, -1.4889808044627912)  # Latitude, Longitude

# Charger le fichier GeoJSON
with open("restaurants.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

filtered_features = []

# Parcourir les restaurants et filtrer ceux à moins de 1 km
for feature in data["features"]:
    restaurant_coords = (feature["geometry"]["coordinates"][1], feature["geometry"]["coordinates"][0])  # (lat, lon)
    distance = geodesic(siao_coords, restaurant_coords).meters  # Distance en mètres
    print(f"Distance entre SIAO et {"nom_restaurant"} : {distance:.2f} m")

    
    if distance <= 1000:  # Moins de 1 km
        feature["properties"]["distance_m"] = round(distance, 2)  # Ajout de la distance
        filtered_features.append(feature)

# Créer un nouveau fichier GeoJSON filtré
filtered_data = {"type": "FeatureCollection", "features": filtered_features}

with open("restaurants_1km.geojson", "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)

print(f"{len(filtered_features)} restaurants trouvés à moins de 1 km du SIAO.")
print("Fichier filtré enregistré sous 'restaurants_1km.geojson'.")

