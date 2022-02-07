#!/usr/bin/env bash
# start_server.sh

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd DaniMundo; python3 manage.py createsuperuser --no-input)
fi
(cd DaniMundo; gunicorn DaniMundo.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"