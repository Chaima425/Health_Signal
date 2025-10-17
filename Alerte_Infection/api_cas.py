from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from datetime import date
from typing import Optional

app = FastAPI(title="API Ajout de Cas")

class Cas(BaseModel):
    id_infection: int
    date_depistage: str
    date_contamination: Optional[str] = None  # <- remplace str | None
    gps: str

# Route POST /cas pour ajouter un cas
@app.post("/cas")
def ajouter_cas(cas: Cas):
    # Vérification simple de la date
    if cas.date_depistage > str(date.today()):
        raise HTTPException(status_code=400, detail="La date de dépistage ne peut pas être dans le futur.")

    # Connexion à la base SQLite
    conn = sqlite3.connect("alerte_infection.db")
    cur = conn.cursor()

    # Vérifier que l'infection existe
    cur.execute("SELECT id FROM infection WHERE id = ?", (cas.id_infection,))
    if cur.fetchone() is None:
        raise HTTPException(status_code=404, detail="Infection non trouvée.")

    # Ins tab cas
    cur.execute("""
        INSERT INTO cas (id_infection, date_depistage, date_contamination)
        VALUES (?, ?, ?)
    """, (cas.id_infection, cas.date_depistage, cas.date_contamination))
    id_cas = cur.lastrowid

    # Ins in tab lieux
    cur.execute("INSERT INTO lieux (id_cas, gps) VALUES (?, ?)", (id_cas, cas.gps))

    conn.commit()
    conn.close()

    return {"message": "Cas ajouté avec succès", "id_cas": id_cas}
