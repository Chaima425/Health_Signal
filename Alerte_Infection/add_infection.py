#add_infection.py
import sqlite3

# Connexion à la base
conn = sqlite3.connect("alerte_infection.db")
cur = conn.cursor()

# Ajout d'une infection test
cur.execute("""
INSERT INTO infection (nom, periode_contagion, periode_incubation, periode_detection, niveau_contagion)
VALUES (?, ?, ?, ?, ?)
""", ("Grippe", 5, 2, 1, 0.5))

conn.commit()
conn.close()
print("Infection test ajoutée avec succès !")
