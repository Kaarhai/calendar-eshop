from base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ['kalendar.draci.info', 'calendar.draci.info'],

INTERNAL_IPS = ['127.0.0.1']

SECRET_KEY = "****"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
