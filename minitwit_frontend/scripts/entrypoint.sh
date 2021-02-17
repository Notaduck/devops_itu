#!/bin/sh

set -e

python manage.py makemigrations
python manage.py migrate
exec "$@"
# ls

# python manage.py collectstatic --noinput

# uwsgi --socket :8000 --master --enable-threads --module app.wsgi