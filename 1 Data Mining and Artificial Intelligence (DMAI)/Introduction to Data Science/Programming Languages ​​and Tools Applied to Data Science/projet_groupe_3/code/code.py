# Importation des bibliothèques

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données
athletes = pd.read_csv("athlete_events.csv")
nocs = pd.read_csv("noc_regions.csv")

df = athletes.merge(nocs, how='left', on='NOC')

sns.set_theme()                           #style agréable pour les graphiques
plt.rcParams['figure.figsize'] = (12, 6)  #définition de la taille par defaut des figures matpltlib a 12 pouces de large et 6 pouces de haut

#Exploration des données
df.shape           # dimensions (lignes, colonnes)
df.columns         # noms des colonnes
df.info()          # types de données et valeurs nulles
df.describe()      # statistiques globales
df.duplicated().sum()   # total de doublons


#Nettoyage des données
#Suppression des doublons
df.drop_duplicates(inplace=True)

# Remplir l'âge manquant par la médiane
df.fillna({"Age" : df["Age"].median()}, inplace=True)

#Remplir la taille et le poids par la moyenne
df.fillna({"Height" : df["Height"].mean()}, inplace=True)
df.fillna({"Weight" : df["Height"].mean()}, inplace=True)


#Visualisatiobn

# 1. Évolution du nombre de participants de 1896 à 2016
participants_par_annee = df.groupby("Year")["ID"].nunique()
plt.figure()
participants_par_annee.plot(marker='o')
plt.title("Évolution du nombre de participants aux JO (1896 - 2016)")
plt.xlabel("Année")
plt.ylabel("Nombre de participants uniques")
plt.tight_layout()
plt.savefig("participants_par_annee.png")
plt.show()

# 2. Participation des femmes
genre_par_annee = df.groupby(["Year", "Sex"])["ID"].nunique().unstack()
plt.figure()
genre_par_annee.plot(marker='o')
plt.title("Participation aux JO : Hommes vs Femmes")
plt.xlabel("Année")
plt.ylabel("Nombre de participants")
plt.legend(["Hommes", "Femmes"])
plt.tight_layout()
plt.savefig("participation_par_sexe.png")
plt.show()

# 3. Répartition des médailles par pays
medailles = df.dropna(subset=["Medal"])
medailles_par_pays = medailles.groupby("region")["Medal"].count().sort_values(ascending=False).head(10)

plt.figure()
medailles_par_pays.plot(kind='bar', color='gold')
plt.title("Top 10 des pays par nombre de médailles")
plt.xlabel("Pays")
plt.ylabel("Nombre de médailles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10_medailles.png")
plt.show()

# 4. Disciplines les plus représentées
disciplines = df["Sport"].value_counts().head(10)
plt.figure()
disciplines.plot(kind='barh', color='skyblue')
plt.title("Top 10 des disciplines les plus représentées")
plt.xlabel("Nombre de participations")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top10_disciplines.png")
plt.show()


# 5. Distribution d’âge des médaillés d’or
gold = athletes[athletes["Medal"] == "Gold"]
plt.figure()
sns.histplot(gold["Age"].dropna(), bins=30, kde=True, color='orange')
plt.title("Distribution des âges des médaillés d’or")
plt.xlabel("Âge")
plt.ylabel("Nombre d'athlètes")
plt.tight_layout()
plt.savefig("age_medailles_or.png")
plt.show()

# Des statistiques concernant le Burkina Faso
# Filtrage les données
burkina_df = df[df['region'] == 'Burkina Faso']

#6 Évolution de la participation du Burkina Faso au fil des ans

plt.figure()
burkina_df.groupby('Year')['ID'].nunique().plot(marker='o')
plt.title("Participation du Burkina Faso aux JO par année")
plt.xlabel("Année")
plt.ylabel("Nombre de participants uniques")
plt.tight_layout()
plt.savefig("burkina_participation_par_annee.png")
plt.show()


#7 Nombre de médailles remportées par le Burkina Faso
medailles_bf = burkina_df[burkina_df['Medal'].notnull()]

if medailles_bf.empty:
    print("Le Burkina Faso n'a remporté aucune médaille durant la période 1896-2016.")
else:
    plt.figure()
    medailles_bf.groupby('Year')['Medal'].count().plot(kind='bar')
    plt.title("Médailles remportées par le Burkina Faso")
    plt.xlabel("Année")
    plt.ylabel("Nombre de médailles")
    plt.tight_layout()
    plt.savefig("burkina_medailles.png")
    plt.show()


#8 Disciplines les plus fréquentes
plt.figure()
burkina_df['Sport'].value_counts().head(10).plot(kind='barh')
plt.title("Disciplines les plus pratiquées par le Burkina Faso")
plt.xlabel("Nombre de participations")
plt.tight_layout()
plt.savefig("burkina_disciplines.png")
plt.show()

#9 Évolution de la participation des femmes
femmes_bf = burkina_df[burkina_df['Sex'] == 'F']

plt.figure()
femmes_bf.groupby('Year')['ID'].nunique().plot(marker='o', color='purple')
plt.title("Participation des femmes du Burkina Faso aux JO")
plt.xlabel("Année")
plt.ylabel("Nombre de participantes uniques")
plt.tight_layout()
plt.savefig("burkina_femmes.png")
plt.show()



