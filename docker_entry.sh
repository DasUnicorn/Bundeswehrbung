#!/bin/sh
poetry run python manage.py migrate --noinput
poetry run gunicorn bundeswehrbung.wsgi -b 0.0.0.0:8000 -w 6