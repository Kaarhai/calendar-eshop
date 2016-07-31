# Calendar Eshop
Eshop for Draci.info dragon calendars and other dragon-related stuff.

## Installation

Prerequisities:

* Python 2.7


Very basic local installation:

    # Create and activate virtualenv.
    mkdir ~/.env
    python -m venv ~/.env/calendareshop
    source ~/.env/calendareshop/bin/activate

    # Upgrade pip.
    pip install --upgrade pip
    
    # Install site and dependencies.
    git clone https://github.com/Draciinfo/calendar-eshop.git
    cd calendar-eshop
    pip install -r requirements.txt

    # Create and edit local settings to match your setup. 
    cd calendareshop
    cp calendareshop/settings/local_[prod|dev]_example.py calendareshop/settings/local.py
    vim calendareshop/settings/local.py

    # Prepare database and load initial data.
    chmod u+x manage.py
    ./manage.py migrate
    ./manage.py loaddata calendareshop/fixtures/sites.json
    ./manage.py loaddata fruit/fixtures/kinds.json
    ./manage.py loaddata staticpage/fixtures/staticpages.json
    ./manage.py createsuperuser
    ./manage.py collectstatic
