import pandas as pd
import mysql.connector
from mysql.connector import errorcode

# Connexion à la base de données MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Utilisateur par défaut de XAMPP MySQL
        password="",  # Mot de passe vide par défaut
        database="football_db"
    )
    cursor = conn.cursor()

    # Lecture des fichiers CSV
    goalscorers_df = pd.read_csv("goalscorers.csv")
    results_df = pd.read_csv("results.csv")

    # Affichage des noms de colonnes pour vérification
    print("Colonnes de goalscorers_df:", goalscorers_df.columns)
    print("Colonnes de results_df:", results_df.columns)

    # Insertion des données dans la table _Match_ (results)
    for index, row in results_df.iterrows():
        cursor.execute("""
            INSERT INTO _Match_ (match_date, tournoi, ville, pays, terrain_neutre)
            VALUES (%s, %s, %s, %s, %s)
        """, (row['date'], row['tournament'], row['city'], row['country'], row['neutral']))
        
        # Récupération de l'ID du match inséré
        match_id = cursor.lastrowid

        # Insertion des données dans la table But (goalscorers) pour ce match
        for _, goal in goalscorers_df[(goalscorers_df['date'] == row['date']) & (goalscorers_df['home_team'] == row['home_team']) & (goalscorers_df['away_team'] == row['away_team'])].iterrows():
            # Vérifier si l'équipe existe dans la table Equipe
            cursor.execute("SELECT equipe_id FROM Equipe WHERE nom = %s", (goal['team'],))
            equipe = cursor.fetchone()

            # Si l'équipe n'existe pas, l'ajouter à la table Equipe
            if not equipe:
                cursor.execute("INSERT INTO Equipe (nom) VALUES (%s)", (goal['team'],))
                equipe_id = cursor.lastrowid
            else:
                equipe_id = equipe[0]

            # Vérifier si le joueur existe dans la table Joueur
            cursor.execute("SELECT joueur_id FROM Joueur WHERE nom = %s AND equipe_id = %s", (goal['scorer'], equipe_id))
            joueur = cursor.fetchone()

            # Si le joueur n'existe pas, l'ajouter à la table Joueur
            if not joueur:
                cursor.execute("INSERT INTO Joueur (nom, equipe_id) VALUES (%s, %s)", (goal['scorer'], equipe_id))
                joueur_id = cursor.lastrowid
            else:
                joueur_id = joueur[0]

            cursor.execute("""
                INSERT INTO But (but_minute, csc, penalty, joueur_id, match_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (goal['minute'], goal['own_goal'], goal['penalty'], joueur_id, match_id))

    # Validation des changements et fermeture de la connexion
    conn.commit()
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erreur de connexion : identifiants incorrects")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Erreur de connexion : base de données inexistante")
    else:
        print(err)
except KeyError as e:
    print(f"Erreur de clé : {e}")
