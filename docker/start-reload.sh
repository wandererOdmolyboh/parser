#!/usr/bin/env sh

echo "Migrations"
python3 manage.py collectstatic --no-input

python3 manage.py migrate
python3 manage.py makemigrations --merge --no-input
python3 manage.py makemigrations --no-input
python3 manage.py migrate


echo "Run server"
python3 manage.py runserver 0.0.0.0:8000 &
celery -A applications.background_tasks.celery_app worker --loglevel=debug &
celery -A applications.background_tasks.celery_app beat --loglevel=debug
