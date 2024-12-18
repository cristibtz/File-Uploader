#!/bin/bash

# Containers to manage
CONTAINERS=("flask_app" "postgres_db")

echo "Checking and stopping containers if they are running..."

# Loop through the containers and stop them if running
for CONTAINER in "${CONTAINERS[@]}"; do
  if [ "$(docker ps -q -f name=${CONTAINER})" ]; then
    echo "Stopping running container: $CONTAINER"
    docker stop "$CONTAINER"
  else
    echo "Container $CONTAINER is not running."
  fi
done

echo "Starting containers..."
# Build and start containers
docker compose up --build &
