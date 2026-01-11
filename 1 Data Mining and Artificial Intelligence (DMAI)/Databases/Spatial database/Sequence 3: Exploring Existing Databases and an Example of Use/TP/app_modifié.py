from flask import Flask, render_template
import random as rand
import math

app = Flask(__name__)


# first route

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/locate-items/<lon>/<lat>') 
def locateItems(lon, lat):
    locations = getLocations(float(lon), float(lat))
    return render_template('map-show.html', longitude = lon, latitude = lat, locations = locations)

def getLocations(ex_lon, ex_lat):
    """
    Génère 10 points aléatoires proches de la position donnée 
    et les trie par distance croissante.
    """
    locations = []
    
    for i in range(10):
        n_lon = ex_lon + (rand.random() - 0.5) / 100  # Décalage aléatoire
        n_lat = ex_lat + (rand.random() - 0.5) / 100
        dist = math.sqrt((ex_lon - n_lon) ** 2 + (ex_lat - n_lat) ** 2) * 111000  # Distance en mètres
        
        locations.append({
            "title": f"Etablissement {i}",
            "detail": f"Elle se trouve à la ville {i}",
            "distance": round(dist, 2),
            "lon": n_lon,
            "lat": n_lat
        })
    
    # Trier les points par distance croissante
    locations.sort(key=lambda loc: loc["distance"])
    
    return locations
  

# keep this as is
if __name__ == '__main__':
    app.run(debug=True)