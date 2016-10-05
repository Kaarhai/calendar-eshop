# -*- coding: utf-8 -*-
"""
Django settings for calendareshop project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.join(os.path.abspath(__file__)))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = None

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

ADMINS = (
    ('Vojtěch Oram', 'flaiming@gmail.com'),
)
ALWAYS_BCC = ['kalendar@draci.info', 'flaiming@gmail.com', 'mail@dragarta.com']
DEFAULT_FROM_EMAIL = "kalendar@draci.info"
SERVER_EMAIL = "vojtech@oram.cz"

EMAIL_USE_TLS = True

SITE_DOMAIN = "draci.info"
SITE_PROTOCOL = "https"

# Application definition

INSTALLED_APPS = (
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'calendareshop',
    'ckeditor',
    'ckeditor_uploader',
    'shopping',
    'plata',
    'plata.contact',
    'plata.discount',
    'plata.payment',
    'plata.shop',
    'bootstrap3',
    'nginx_image',
    'adminsortable',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'calendareshop.middleware.SubdomainLanguageMiddleware'
)

ROOT_URLCONF = 'calendareshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'calendareshop.context_processors.project_types',
                'calendareshop.context_processors.site',
                'plata.context_processors.plata_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'calendareshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dbfile',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'cs'

gettext = lambda s: s
LANGUAGES = (
    ('cs', gettext('Czech')),
    ('en', gettext('English')),
)

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = False

SITE_ID = 1

DATE_FORMAT = "j. E Y"

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_DIR = "media"
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_DIR)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "..", "static")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': "%(levelname)s %(message)s"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'maxBytes': 16 * 1024 * 1024,  # 16megabytes
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['log_file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['log_file', 'console'],
            'level': 'DEBUG',
        },
    }
}

# Caching
if not DEBUG:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

# CKEditor
CKEDITOR_JQUERY_URL = "/static/js/jquery.js"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': ','.join(
            [
                # your extra plugins here
                'pastefromword'
            ]),
    }
}

SUBDOMAIN_LANGUAGES = {
    'kalendar': 'cs',
    'calendar': 'en'
}

# plata
PLATA_SHOP_PRODUCT = 'shopping.Product'
CURRENCIES = ('CZK', 'EUR', 'USD')
CURRENCY_FORMATS = {
    'CZK': u'{0:.2f} Kč',
    'EUR': u'€ {0:.2f}',
    'USD': u'$ {0:.2f}',
}
DEFAULT_CURRENCY_FOR_LANG = {
    'cs': 'CZK',
    'en': 'EUR'
}
CURRENCY_SESSION_KEY = 'draciinfocalendar_currency'

PLATA_PAYMENT_MODULES = (
    'plata.payment.modules.cod.PaymentProcessor',
    'shopping.payment_modules.bank.PaymentProcessor',
    'shopping.payment_modules.cash.PaymentProcessor',
    'plata.payment.modules.paypal.PaymentProcessor',
)

PLATA_PAYMENT_COD = u'cod'
PLATA_PAYMENT_BANK = u'bank'
PLATA_PAYMENT_CASH = u'cash'
PLATA_PAYMENT_PAYPAL = u'paypal'
PLATA_PAYMENT_MODULE_NAMES = {
    PLATA_PAYMENT_COD: gettext(u"Cash on delivery"),
    PLATA_PAYMENT_BANK: gettext(u"Bank transfer"),
    PLATA_PAYMENT_CASH: gettext(u"Cash"),
    PLATA_PAYMENT_PAYPAL: gettext(u"PayPal"),
}

PLATA_REPORTING_ADDRESSLINE = u"""Vojtěch Oram
I.J.Pešiny 2600
Frýdek-Místek
738 01"""
PLATA_REPORTING_STATIONERY = 'calendareshop.pdfdocument.InvoiceStationery'
PLATA_PDF_FONT_NAME = 'DejaVuSans'
PLATA_PDF_FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
PLATA_PDF_FONT_BOLD_NAME = 'DejaVuSans-Bold'
PLATA_PDF_FONT_BOLD_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

PAYPAL = {
    'LIVE': True,  # Use sandbox or live payment interface?
    'BUSINESS': 'flaiming@gmail.com',
}
PAYPAL_TRANSACTION_PRICES = {
    'CZK': 10.0,
    'EUR': 0.35,
    'USD': 0.3
}

PLATA_ORDER_PROCESSORS = [
    'plata.shop.processors.InitializeOrderProcessor',
    'plata.shop.processors.DiscountProcessor',
    'plata.shop.processors.TaxProcessor',
    'plata.shop.processors.MeansOfPaymentDiscountProcessor',
    'plata.shop.processors.ItemSummationProcessor',
    'plata.shop.processors.ZeroShippingProcessor',
    'shopping.processors.ShippingProcessor',
    'shopping.processors.PaymentProcessor',
    'plata.shop.processors.OrderSummationProcessor',
]

from decimal import Decimal
TAX = Decimal('21.0')

PAYMENT_BANK_ATTRS = {
    'bank_account_no': '2901050776',
    'bank_no': '2010',
}

import datetime
PREORDER_END = datetime.date(2016, 10, 24)
