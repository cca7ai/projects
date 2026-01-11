import pandas as pd
import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="football_db"
)
cursor = conn.cursor()

# Fonction pour charger les fichiers CSV avec gestion d'encodage
def load_csv(file_path):
    try:
        df = pd.read_csv(file_path, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding="latin1")

    # Normalisation des noms de colonnes
    df.columns = df.columns.str.lower()
    
    # Affichage des premières lignes et des colonnes disponibles
    print(f"\n📌 Contenu du fichier {file_path} :")
    print(df.head())
    print(f"\n📌 Colonnes disponibles dans {file_path} :")
    print(df.columns)

    return df

# Charger les fichiers CSV
results_df = load_csv("results.csv")
goalscorers_df = load_csv("goalscorers.csv")

# Vérifier que les colonnes clés existent
required_columns = ["date", "home_team", "away_team"]
for col in required_columns:
    if col not in goalscorers_df.columns:
        raise KeyError(f"Erreur: La colonne '{col}' est absente du fichier goalscorers.csv.")

# Ajouter "tournament" et "country" à goalscorers_df en faisant une jointure avec results_df
goalscorers_df = goalscorers_df.merge(
    results_df[["date", "home_team", "away_team", "tournament", "country"]],
    on=["date", "home_team", "away_team"],
    how="left"
)

# Vérification après fusion
print("\n📌 goalscorers_df après ajout des colonnes 'tournament' et 'country' :")
print(goalscorers_df.head())

# Vérifier si la jointure a échoué pour certaines lignes
missing_tournament = goalscorers_df[goalscorers_df["tournament"].isna()]
if not missing_tournament.empty:
    print("\n⚠️ Certaines lignes n'ont pas pu récupérer 'tournament' et 'country' :")
    print(missing_tournament)

# Fonction pour insérer une équipe et récupérer son ID
def get_or_create_team(nom):
    cursor.execute("SELECT equipe_id FROM Equipe WHERE nom = %s", (nom,))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute("INSERT INTO Equipe (nom) VALUES (%s)", (nom,))
    conn.commit()
    return cursor.lastrowid

# Fonction pour insérer un joueur et récupérer son ID
def get_or_create_player(nom, equipe_id):
    cursor.execute("SELECT joueur_id FROM Joueur WHERE nom = %s AND equipe_id = %s", (nom, equipe_id))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute("INSERT INTO Joueur (nom, equipe_id) VALUES (%s, %s)", (nom, equipe_id))
    conn.commit()
    return cursor.lastrowid

# Insertion des matchs
for _, row in results_df.iterrows():
    equipe1_id = get_or_create_team(row["home_team"])
    equipe2_id = get_or_create_team(row["away_team"])
    
    cursor.execute(
        """
        INSERT INTO _Match_ (match_date, tournoi, ville, pays, terrain_neutre)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (row["date"], row["tournament"], row["city"], row["country"], row["neutral"])
    )
    conn.commit()
    match_id = cursor.lastrowid
    
    # Liaison match-équipe
    cursor.execute("INSERT INTO participe (match_id, equipe_id) VALUES (%s, %s)", (match_id, equipe1_id))
    cursor.execute("INSERT INTO participe (match_id, equipe_id) VALUES (%s, %s)", (match_id, equipe2_id))
    conn.commit()

# Insertion des buteurs
for _, row in goalscorers_df.iterrows():
    cursor.execute(
        "SELECT match_id FROM _Match_ WHERE match_date = %s AND tournoi = %s AND pays = %s",
        (row["date"], row["tournament"], row["country"])
    )
    match_result = cursor.fetchone()
    if match_result:
        match_id = match_result[0]
        equipe_id = get_or_create_team(row["team"])
        joueur_id = get_or_create_player(row["scorer"], equipe_id)
        
        cursor.execute(
            """
            INSERT INTO But (but_minute, csc, penalty, match_id, joueur_id)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (row["minute"], row["own_goal"], row["penalty"], match_id, joueur_id)
        )
        conn.commit()

cursor.close()
conn.close()
print("\n✅ Données insérées avec succès !")
