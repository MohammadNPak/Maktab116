#!/bin/sh
python manage.py makemigrations
python manage.py migrate

celery -A core worker --loglevel=info &
python manage.py runserver 0.0.0.0:8000