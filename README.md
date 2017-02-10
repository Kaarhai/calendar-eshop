# Calendar Eshop
Eshop for Draci.info dragon calendars and other dragon-related stuff.

## Installation

Prerequisities:

* Python 2.7


Very basic local installation:
```python
# Create and activate virtualenv.
mkdir ~/calendar-eshop  # or where you want it to be
cd ~/calendar-eshop
# if not already installed, install virtualenv and activate it.
pip install virtualenv
virtualenv .
source bin/activate

# Install site and dependencies.
git clone https://github.com/Draciinfo/calendar-eshop.git
cd calendar-eshop 
pip install -r requirements.txt

# install developement requirements if needed
pip install -r requirements_dev.txt

# Create and edit local settings to match your setup. 
cd calendareshop
cp calendareshop/settings/local_[prod|dev]_example.py calendareshop/settings/local.py
vim calendareshop/settings/local.py

# Prepare database and load initial data.
./manage.py migrate
./manage.py createsuperuser
./manage.py collectstatic
```
