#! /usr/bin/env bash

# Let the DB start
python /levers/app/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python /levers/app/initial_data.py