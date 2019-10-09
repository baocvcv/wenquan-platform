#!/bin/sh
python manage.py migrate
gunicorn 'WenQuan_Platform.wsgi' -b 0.0.0.0:80 --access-logfile - --log-level info
