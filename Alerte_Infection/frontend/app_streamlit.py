import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"  # Ton API FastAPI

st.title("Dashboard Alerte Infection")

# ----------------------------
# Ajouter un cas
# ----------------------------
st.header("Ajouter un nouveau cas")
with st.form(key="form_cas"):
    id_infection = st.number_input("ID de l'infection", min_value=1, step=1)
    date_depistage = st.date_input("Date de dépistage")
    date_contamination = st.date_input("Date de contamination (optionnel)", value=None)
    gps_input = st.text_input("GPS (séparés par un point-virgule)", "43.611,3.877;43.612,3.879")
    submit_btn = st.form_submit_button("Ajouter le cas")

if submit_btn:
    gps_list = [g.strip() for g in gps_input.split(";") if g.strip()]
    data = {
        "id_infection": id_infection,
        "date_depistage": date_depistage.isoformat(),
        "date_contamination": date_contamination.isoformat() if date_contamination else None,
        "gps_list": gps_list
    }
    try:
        response = requests.post(f"{API_BASE}/cas", json=data)
        if response.status_code == 200:
            st.success("Cas ajouté avec succès !")
            st.json(response.json())
        else:
            st.error(f"Erreur {response.status_code}: {response.json()}")
    except Exception as e:
        st.error(f"Impossible de contacter l'API : {e}")

# ----------------------------
# Afficher la liste des cas
# ----------------------------
st.header("Liste des cas")
if st.button("Charger les cas"):
    try:
        response = requests.get(f"{API_BASE}/cas")
        if response.status_code == 200:
            cas_list = response.json().get("cas", [])
            for c in cas_list:
                st.write(f"ID: {c['id_cas']}, Infection: {c['id_infection']}, Date dépistage: {c['date_depistage']}, Lieux: {', '.join(c['lieux'])}")
        else:
            st.error(f"Erreur {response.status_code}")
    except Exception as e:
        st.error(f"Impossible de récupérer les cas : {e}")

# ----------------------------
# Afficher les notifications
# ----------------------------
st.header("Notifications")
if st.button("Charger les notifications"):
    try:
        response = requests.get(f"{API_BASE}/notifications")
        if response.status_code == 200:
            notifs = response.json().get("notifications", [])
            for n in notifs:
                st.write(f"[{n['date_creation']}] {n['message']}")
        else:
            st.error(f"Erreur {response.status_code}")
    except Exception as e:
        st.error(f"Impossible de récupérer les notifications : {e}")
