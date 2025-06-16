#!/bin/sh
# entrypoint.sh
# Este script se ejecuta cuando el contenedor inicia.
# Sirve para realizar tareas iniciales (como migraciones) antes de levantar el servidor.

# Muestra los comandos a medida que se ejecutan y termina en caso de error.
set -xe
# Ejecuta las migraciones de base de datos.
python manage.py migrate --noinput
# traido de dockerfile para no tener conflicto
python manage.py collectstatic --noinput --clear
# Levanta el servidor Gunicorn, reemplazando este script con Gunicorn (para que reciba correctamente señales de Docker).
exec gunicorn settings_app.wsgi:application --bind 0.0.0.0:8000

# ejecutar chmod +x entrypoint.sh