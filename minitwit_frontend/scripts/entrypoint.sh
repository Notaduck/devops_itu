#!/bin/sh

set -e

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

uwsgi -b 32768 --socket :8000 --master --enable-threads --module minitwit.wsgi

# python manage.py makemigrations
# python manage.py migrate
# exec "$@"
# ls
