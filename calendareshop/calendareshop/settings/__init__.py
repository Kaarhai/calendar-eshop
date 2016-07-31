from django.core.exceptions import ImproperlyConfigured

try:
    from .local import *  # noqa
except ImportError:
    raise ImproperlyConfigured('Please provide instance-specific settings/local.py '
                               '(see settings/local_example.py).')

if not SECRET_KEY or SECRET_KEY.startswith('****'):
    raise ImproperlyConfigured('Please set SECRET_KEY in settings/local.py '
                               'to a unique, unpredictable value.')
