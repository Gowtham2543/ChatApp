#!/bin/bash

# Script to start the development server
# !!! Dont use in production

export FLASK_APP=./app.py
export PIPENV_VERBOSITY=-1

[ -z $1 ] && pipenv run flask --debug run -h 0.0.0.0

! [ -z $1 ] && pipenv run gunicorn -w 4 -b 0.0.0.0:5000 app:app