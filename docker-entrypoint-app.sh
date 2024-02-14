#!/bin/bash

# Apply database migrations
python manage.py migrate

# Start Django server
exec python manage.py runserver 0.0.0.0:8000