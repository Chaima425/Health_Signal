# Health_Signal – POC

## Description
Ce projet est un **Proof of Concept (POC)** pour un système de communication entre professionnels de santé, agences et public afin de gérer les cas de maladies infectieuses.

---

## Composant : Formulaire d’ajout de cas

### Fonctionnalité
Permet aux professionnels de santé d’ajouter un **nouveau cas infectieux** via un formulaire web. Les données sont envoyées à l’API `/cas`.

### Données collectées
- `id_infection` : ID de l’infection concernée  
- `date_depistage` : date du dépistage (doit être ≤ aujourd’hui)  
- `date_contamination` (optionnelle) : date supposée de contamination  
- `gps` : coordonnées GPS des lieux fréquentés

### Validation
- La date de dépistage **ne peut pas être dans le futur**  
- Vérification que l’infection existe dans la table `infection`

### Stockage
- Données enregistrées dans la base SQLite `alerte_infection.db`  
- Table `cas` pour le cas  
- Table `lieux` pour les coordonnées GPS associées

### Lien avec l’API
- Endpoint backend : `POST /cas`  
- Reçoit un JSON conforme au modèle **`Cas`** défini avec Pydantic

---

## Installation

1. Créer un environnement virtuel :  
```bash
python3 -m venv .venv
source .venv/bin/activate
2. Installer les dependances :
'''bash pip install fastapi uvicorn pydantic sqlite3
'''
3.Lancer le serveur FastApi : 
uvicorn api_cas:app --reload


