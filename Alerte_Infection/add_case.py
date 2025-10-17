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

# 3️ Add un lieu lié à ce cas
cur.execute("""
INSERT INTO lieux (id_cas, gps) VALUES (1, '43.611,3.877')
""")

conn.commit()
conn.close()
print(" Cas et lieu ajoutés avec succès !")
