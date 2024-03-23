#!/bin/bash

# Attempt till max_attempts to do migrations
attempts=0
max_attempts=5
retry_delay=15

while [ $attempts -lt $max_attempts ]; do
    attempts=$((attempts + 1))
    echo "Attempting to apply migrations (Attempt $attempts of $max_attempts)..."
    python /project/exam_project/manage.py migrate --noinput && break
    echo "Migration attempt failed. Retrying in $retry_delay seconds..."
    sleep $retry_delay
done

# Start Django server
exec python /project/exam_project/manage.py runserver 0.0.0.0:8000