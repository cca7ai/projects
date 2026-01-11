from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["TP0"]

# Collection des étudiants
etudiants = db["etudiants"]
etudiants.insert_many([
    {
        "nom": "Sawadogo",
        "prenoms": "Habibou Michel",
        "date_naissance": "1998-07-15",
        "adresse": {
            "rue": "Avenue Kwame Nkrumah",
            "ville": "Ouagadougou",
            "pays": "Burkina Faso"
        },
        "telephone": "+226 70 12 34 56",
        "notes": [
            { "matiere": "Mathématiques", "note": 16.5 },
            { "matiere": "Physique", "note": 14.0 },
            { "matiere": "Informatique", "note": 18.0 }
        ]
    },
    {
        "nom": "Ouédraogo",
        "prenoms": "Fatimata",
        "date_naissance": "2000-03-25",
        "adresse": {
            "rue": "Rue de l’Université",
            "ville": "Ouagadougou",
            "pays": "Burkina Faso"
        },
        "telephone": "+226 76 89 12 34",
        "notes": [
            { "matiere": "Littérature", "note": 15.0 },
            { "matiere": "Histoire", "note": 16.5 },
            { "matiere": "Anglais", "note": 17.0 }
        ]
    }
])

# Collection des universités
universites = db["universites"]
universites.insert_many([
    {
        "nom": "Université Joseph Ki-Zerbo",
        "ville": "Ouagadougou",
        "pays": "Burkina Faso",
        "adresse": "Avenue Charles De Gaulle",
        "telephone": "+226 25 30 70 64",
        "site_web": "http://www.univ-ouaga.bf",
        "formations": [
            { "nom": "Informatique", "niveau": "Licence" },
            { "nom": "Droit", "niveau": "Master" },
            { "nom": "Médecine", "niveau": "Doctorat" }
        ]
    },
    {
        "nom": "Université Aube Nouvelle",
        "ville": "Ouagadougou",
        "pays": "Burkina Faso",
        "adresse": "Avenue de la Liberté",
        "telephone": "+226 25 37 47 58",
        "site_web": "http://www.aubenouvelle.edu.bf",
        "formations": [
            { "nom": "Gestion", "niveau": "Licence" },
            { "nom": "Marketing", "niveau": "Master" },
            { "nom": "Ressources Humaines", "niveau": "Doctorat" }
        ]
    }
])

print("Données insérées avec succès !")

