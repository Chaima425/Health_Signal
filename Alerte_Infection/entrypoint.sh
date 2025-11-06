#!/bin/sh
set -e

# Si Azure ne donne pas de port → 8501 par défaut
PORT_NUMBER=${PORT:-8501}

echo "🔧 Using PORT=$PORT_NUMBER"

# démarrer FastAPI en background sur 8000 (interne)
uvicorn api_cas:app --host 0.0.0.0 --port 8000 --log-level info &

# attendre API lançée (max 15s)
tries=0
until curl -sS http://127.0.0.1:8000/ > /dev/null 2>&1 || [ $tries -ge 15 ]; do
    tries=$((tries+1))
    echo "Waiting for API to be available... ($tries)"
    sleep 1
done

echo " API OK → Start Streamlit..."

# Streamlit écoute sur PORT Azure
exec streamlit run frontend/app_streamlit.py \
    --server.port $PORT_NUMBER \
    --server.address 0.0.0.0 \
    --server.headless true


# set -e

# PORT_NUMBER=${PORT:-8501}
# export STREAMLIT_SERVER_PORT="$PORT_NUMBER"
# export STREAMLIT_SERVER_ADDRESS="0.0.0.0"

# # Démarre FastAPI en arrière-plan
# uvicorn api_cas:app --host 0.0.0.0 --port 8000 --log-level info &

# # Attente que l'API soit disponible
# tries=0
# until curl -sS http://127.0.0.1:8000/ > /dev/null 2>&1 || [ $tries -ge 15 ]; do
#     tries=$((tries+1))
#     echo "Waiting for API to be available... ($tries)"
#     sleep 1
# done

# # Démarre Streamlit sur le port injecté par Azure
# exec streamlit run frontend/app_streamlit.py \
#     --server.port $PORT_NUMBER \
#     --server.address 0.0.0.0 \
#     --server.headless true \
#     --server.enableCORS false \
#     --server.enableXsrfProtection false


