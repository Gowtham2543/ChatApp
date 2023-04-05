#!/bin/bash

# Run this file if any modifications is done to the models

python3 dropDB.py #Drops all the tables in the DB

python3 createDB.py #Creates all the schemas