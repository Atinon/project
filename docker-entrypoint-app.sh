#!/bin/bash

# Apply database migrations
python /project/exam_project/manage.py migrate

# Start Django server
exec python /project/exam_project/manage.py runserver 0.0.0.0:8000