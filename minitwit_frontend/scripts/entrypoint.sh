#!/bin/sh
set -e

python manage.py makemigrations
python manage.py makemigrations latest
python manage.py migrate

su - user
python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module minitwit_frontend.wsgi
