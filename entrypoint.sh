#!/usr/bin/env sh
set -e

echo "APP_ENV=$APP_ENV"

if [ "$APP_ENV" = "dev" ]; then
  echo "Starting FastAPI dev server..."
  exec fastapi dev main.py --host 0.0.0.0 --port "${PORT:-5000}"
else
  echo "Starting Uvicorn (prod)..."
  exec fastapi run main.py --host 0.0.0.0 --port "${PORT:-5000}"
fi