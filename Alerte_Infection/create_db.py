#create_db.py
import sqlite3
from datetime import date

# Connexion / création de la base
conn = sqlite3.connect("alerte_infection.db")
cur = conn.cursor()

# Supprimer les tables si elles existent déjà
cur.executescript("""
DROP TABLE IF EXISTS lieux;
DROP TABLE IF EXISTS cas;
DROP TABLE IF EXISTS infection;
DROP TABLE IF EXISTS notifications;
""")

# Table infection
cur.execute("""
CREATE TABLE infection (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    periode_contagion INTEGER CHECK(periode_contagion > 0),
    periode_incubation INTEGER CHECK(periode_incubation > 0),
    periode_detection INTEGER CHECK(periode_detection > 0),
    niveau_contagion REAL CHECK(niveau_contagion BETWEEN 0 AND 1)
);
""")

# Table cas
cur.execute("""
CREATE TABLE cas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_infection INTEGER NOT NULL,
    date_depistage TEXT NOT NULL,
    date_contamination TEXT,
    FOREIGN KEY (id_infection) REFERENCES infection(id)
);
""")

# Table lieux
cur.execute("""
CREATE TABLE lieux (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cas INTEGER NOT NULL,
    gps TEXT NOT NULL,
    FOREIGN KEY (id_cas) REFERENCES cas(id)
);
""")
#Tab notifications
cur.execute("""
CREATE TABLE notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cas INTEGER NOT NULL,
    message TEXT NOT NULL,
    date_notification TEXT DEFAULT CURRENT_TIMESTAMP,
    statut TEXT DEFAULT 'non lue',
    FOREIGN KEY (id_cas) REFERENCES cas(id)
);
""")

conn.commit()
conn.close()
print("Base de données créée avec succès")
