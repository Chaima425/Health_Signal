#add_case.py
import sqlite3
from datetime import date

conn = sqlite3.connect("alerte_infection.db")
cur = conn.cursor()

# 1️ add une infection (if aucune infection n’existe)
cur.execute("""
INSERT INTO infection (nom, periode_contagion, periode_incubation, periode_detection, niveau_contagion)
VALUES ('Grippe', 5, 2, 3, 0.8)
""")

# 2️ Add un cas (check:  la date de dépistage <= aujourd’hui)
cur.execute("""
INSERT INTO cas (id_infection, date_contamination, date_depistage)
VALUES (1, '2025-10-10', '2025-10-17')
""")
id_cas = cur.lastrowid  # récupérer l'ID du cas ajouté

# 3️ Ajouter plusieurs lieux liés à ce cas
gps_list = ['43.611,3.877', '43.612,3.879', '43.615,3.880']  # liste des lieux
for gps in gps_list:
    cur.execute("INSERT INTO lieux (id_cas, gps) VALUES (?, ?)", (id_cas, gps))



conn.commit()
conn.close()
print(" Cas et lieux ajoutés avec succès !")
