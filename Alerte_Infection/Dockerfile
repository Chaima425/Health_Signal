# Image Python légère
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY . /app

# Mettre pip à jour et installer les dépendances
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Commande de démarrage adaptée à Azure
CMD streamlit run frontend/app_streamlit.py --server.port=$PORT --server.address=0.0.0.0




# # Utiliser une image Python officielle
# FROM python:3.11-slim

# # Installer pip si nécessaire
# RUN python -m ensurepip --upgrade

# # Copier le projet
# WORKDIR /app

# COPY . /app

# # Installer les dépendances
# RUN python -m pip install --upgrade pip
# RUN python -m pip install -r requirements.txt

# # Installer seulement les paquets nécessaires
# RUN pip install --no-cache-dir streamlit pandas

# # Exposer le port dynamique (valeur par défaut si PORT non défini)
# ENV PORT=8501

# CMD streamlit run frontend/app_streamlit.py --server.port=$PORT --server.address=0.0.0.0

