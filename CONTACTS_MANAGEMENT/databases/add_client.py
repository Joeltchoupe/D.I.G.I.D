import psycopg2
from psycopg2 import sql

# Remplacez ces informations par les détails de votre base de données
DATABASE_NAME = "votre_nom_de_bdd"
USER = "votre_utilisateur"
PASSWORD = "votre_mot_de_passe"
HOST = "votre_hote"
PORT = "votre_port"

# Connexion à la base de données
conn = psycopg2.connect(
    dbname=DATABASE_NAME,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT
)

# Création d'un curseur
cur = conn.cursor()

# Exemple d'insertion de données
cur.execute("""
    INSERT INTO Client (Nom, Prenom, DateNaissance, Sexe, AdressePostale, AdresseEmail, NumeroTelephone,
                       NumeroSecuriteSociale, EtatCivil, SituationFamiliale, Nationalite, Profession, Revenu,
                       SituationPatrimoniale)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", ('Doe', 'John', '1990-01-01', 'M', '123 Rue de la Banque', 'john.doe@email.com', '123456789', 
      '123-45-6789', 'Célibataire', 'Sans enfants', 'Française', 'Banquier', 80000.00, 'Aucune'))

# Exemple de requête de sélection
cur.execute("SELECT * FROM Client;")
rows = cur.fetchall()

# Affichage des résultats
for row in rows:
    print(row)

# Fermeture du curseur et de la connexion
cur.close()
conn.close()
