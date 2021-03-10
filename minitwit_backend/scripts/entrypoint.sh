#!/bin/sh
set -e

python manage.py makemigrations
python manage.py migrate

uwsgi --socket :9000 --master --enable-threads --module minitwit_backend.wsgi
