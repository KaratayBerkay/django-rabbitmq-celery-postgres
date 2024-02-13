#!/bin/sh

UWSGI_UID=uwsgi
echo 'Run migration'
python manage.py makemigrations || echo "No makemigrations found"
#python manage.py makemigrations polls || echo "No makemigrations found"
python manage.py migrate || echo "Nothing to migrate"
python manage.py createsuperuser --noinput || echo "Super user already created"
echo 'Collect Static'
python manage.py collectstatic --noinput || echo "No static to collect"
echo 'Run server'
mkdir "/var/log/uwsgi" || echo "Log folder already created"
adduser $UWSGI_UID || echo "User already created"
chmod +x ./uwsgi.ini
uwsgi --ini uwsgi.ini --uid $UWSGI_UID
exec "$@"