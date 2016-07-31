#!/bin/sh
#
# Script for deploying new changes in production.

set -ex

# save credentials for later use
sudo -v

git fetch
git merge --ff-only origin/master

# migrate database
./manage.py migrate

# collect static and compress
./manage.py collectstatic --noinput
#./manage.py compress

touch confs/production/uwsgi.ini
