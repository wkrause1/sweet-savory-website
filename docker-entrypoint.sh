#!/bin/bash

python manage.py migrate 

if [ -z "${PORT}" ]; then 
    PORT=8000
fi

python manage.py runserver 0.0.0.0:${PORT}