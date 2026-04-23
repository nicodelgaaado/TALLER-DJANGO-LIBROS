#!/usr/bin/env bash
set -o errexit

# Install Python dependencies required by manage.py commands.
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate --noinput
