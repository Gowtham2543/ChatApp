#!/bin/bash

# Script to start the development server
# !!! Dont use in production

export FLASK_APP=./app.py
export PIPENV_VERBOSITY=-1

pipenv run flask --debug run -h 0.0.0.0