#!/bin/sh
python manage.py makemigrations
python manage.py migrate --fake
gunicorn 'WenQuan_Platform.wsgi' -b 0.0.0.0:80 --access-logfile - --log-level info
