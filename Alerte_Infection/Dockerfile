# 1. Image de base
# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Copy requirements and install
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt 
# RUN apt-get install -y curl 
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Create a non-root user (optional but recommended)
RUN adduser --disabled-password --gecos "" appuser || true
RUN chown -R appuser:appuser /app

# Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Passer à l'utilisateur non-root
USER appuser

# Expose streamlit default port (Azure will map $PORT)
# EXPOSE 8501 8000

# Entrypoint
ENTRYPOINT ["/entrypoint.sh"]







# FROM python:3.12-slim

# # 2. Répertoire de travail: /app ou /src apres il fait cd app 
# WORKDIR /app

# # 3. Copier requirements et installer les dépendances
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # 4. Copier le code de l'application : copier la source et la destination si j'avais des dossier n'est veux pas copier on mettre en dockerignore exp : .env et logging 
# COPY . .

# # 5. Exposer le port (Azure utilisera $PORT)
# EXPOSE 8501

# # 6. Copier le script d'entrée et rendre exécutable
# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

# # 7. Définir le point d'entrée soit cmd soit entrypoint si on utilise CMd : CMD ["streamlit", "run", "frontend/app_streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"] ou serveur : localhost
# ENTRYPOINT ["/entrypoint.sh"]




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

