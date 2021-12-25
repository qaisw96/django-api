web: gunicorn django_project.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate

web: gunicorn --bind 0.0.0.0:$PORT project_name:ap