#!/bin/bash
rm -rf raterprojectapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations raterprojectapi
python manage.py migrate raterprojectapi
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata categories
python manage.py loaddata gamers
python manage.py loaddata games
python manage.py loaddata game_categories
python manage.py loaddata images
python manage.py loaddata ratings
python manage.py loaddata reviews