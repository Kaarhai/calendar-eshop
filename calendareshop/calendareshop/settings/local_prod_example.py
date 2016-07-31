from base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ['kalendar.chcidraky.cz', 'calendar.chcidraky.cz'],

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
