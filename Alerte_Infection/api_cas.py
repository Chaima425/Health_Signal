#api_cas.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from datetime import date
from typing import Optional, List

app = FastAPI(title="API Ajout de Cas")

class Cas(BaseModel):
    id_infection: int
    date_depistage: str
    date_contamination: Optional[str] = None
    gps_list: List[str]  # m plusieurs lieux possibles

@app.get("/")
def read_root():
    return {"message": "API Alerte Infection opérationnelle"}

@app.post("/cas")
def ajouter_cas(cas: Cas):
    if cas.date_depistage > str(date.today()):
        raise HTTPException(status_code=400, detail="La date de dépistage ne peut pas être dans le futur.")

    conn = sqlite3.connect("alerte_infection.db", timeout=10)
    cur = conn.cursor()

    # Vérifier que l'infection existe
    cur.execute("SELECT id FROM infection WHERE id = ?", (cas.id_infection,))
    if cur.fetchone() is None:
        raise HTTPException(status_code=404, detail="Infection non trouvée.")

    # # Insérer le cas
    cur.execute("""
        INSERT INTO cas (id_infection, date_depistage, date_contamination)
        VALUES (?, ?, ?)
    """, (cas.id_infection, cas.date_depistage, cas.date_contamination))
    id_cas = cur.lastrowid

    # la liste des GPS
    for gps in cas.gps_list:
        cur.execute("INSERT INTO lieux (id_cas, gps) VALUES (?, ?)", (id_cas, gps))

    ## Créer une notification
    notif_message = f"Nouveau cas ajouté : id {id_cas}, infection {cas.id_infection}"
    cur.execute("INSERT INTO notifications (id_cas, message) VALUES (?, ?)", (id_cas, notif_message))

    conn.commit()
    conn.close()

    return {"message": "Cas ajouté avec succès", "id_cas": id_cas}

# ==============================
# Route GET /notifications : Récupérer les notifications
# ==============================
@app.get("/notifications")
def get_notifications():
    conn = sqlite3.connect("alerte_infection.db")
    cur = conn.cursor()
    cur.execute("""
    SELECT id, message, date_notification
    FROM notifications
    ORDER BY date_notification DESC
""")

    notifs = cur.fetchall()
    conn.close()

    # Transformer en dictionnaires
    return {"notifications": [
    {"id": n[0], "message": n[1], "date_creation": n[2]} for n in notifs
]}
@app.get("/cas")
def get_all_cas():
    conn = sqlite3.connect("alerte_infection.db")
    cur = conn.cursor()

    # Récupérer tous les cas
    cur.execute("""
        SELECT c.id, c.id_infection, c.date_depistage, c.date_contamination
        FROM cas c
        ORDER BY c.id DESC
    """)
    cas_list = cur.fetchall()

    # Pour chaque cas, récupérer les lieux
    result = []
    for cas in cas_list:
        id_cas, id_infection, date_depistage, date_contamination = cas
        cur.execute("SELECT gps FROM lieux WHERE id_cas = ?", (id_cas,))
        lieux = [l[0] for l in cur.fetchall()]
        result.append({
            "id_cas": id_cas,
            "id_infection": id_infection,
            "date_depistage": date_depistage,
            "date_contamination": date_contamination,
            "lieux": lieux
        })

    conn.close()
    return {"cas": result}