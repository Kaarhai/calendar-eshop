#!/bin/sh
#
# Script for deploying new changes in production.

PROJECT_PATH=/www/calendar-eshop/calendar-eshop/calendareshop

set -ex

# save credentials for later use
#sudo -v

git fetch
git merge --ff-only origin/master

# install requirements
pip install -r ../requirements.txt

# migrate database
./manage.py migrate

# collect static and compress
./manage.py collectstatic --noinput
#./manage.py compress

# update cron
cp $PROJECT_PATH/calendareshop.cron /etc/cron.d/calendareshop.cron
crontab /etc/cron.d/calendareshop.cron
/etc/init.d/cron reload 

touch confs/production/uwsgi.ini
