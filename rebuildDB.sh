#!/bin/bash
export PIPENV_VERBOSITY=-1
# Run this file if any modifications is done to the models

pipenv run python3 dropDB.py #Drops all the tables in the DB

pipenv run python3 createDB.py #Creates all the schemas