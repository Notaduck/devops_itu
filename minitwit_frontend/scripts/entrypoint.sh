#!/bin/sh

set -e
ls

python manage.py collectstatic --noinput

uwsgi --socker :8000 --master --enable-threads --module app.wsgi