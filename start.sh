#!/bin/bash

# Script to start the development server or wsgi server
# !!! Dont use in production

# Pass no argument to start the development server
# Pass any argument to start the wsgi server

export FLASK_APP=./app.py
export PIPENV_VERBOSITY=-1

[ -z $1 ] && pipenv run flask --debug run -h 0.0.0.0

! [ -z $1 ] && pipenv run gunicorn -w 4 -b 0.0.0.0:5000 app:app