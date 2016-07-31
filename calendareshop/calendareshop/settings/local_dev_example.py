from base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

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

# add debug toolbar
INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
    'django_extensions',
)
MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
#LOGGING['loggers']['django.db.backends']['level'] = 'DEBUG'


EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/www/draciprojekty/draciprojekty/logs/'
