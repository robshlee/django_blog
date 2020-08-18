#!/bin/bash
python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn django_blog.wsgi:application --bind 0.0.0.0:8000 --workers=4 -t 300