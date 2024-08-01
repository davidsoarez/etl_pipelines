#!/bin/bash

echo "Waiting PostgreSQL..."
while ! nc -z postgres 5432; do
  sleep 1
done
echo "PostgreSQL started"

alembic upgrade head

python main.py

tail -f /dev/null