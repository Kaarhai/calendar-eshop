from django.conf import settings
from django.utils.translation import get_language


def get_currency_code(request=None):
    if request:
        for attr in ('session', 'COOKIES'):
            if hasattr(request, attr):
                try:
                    return getattr(request, attr)[settings.CURRENCY_SESSION_KEY]
                except KeyError:
                    continue

        lang = request.LANGUAGE_CODE
        if lang in settings.DEFAULT_CURRENCY_FOR_LANG:
            return settings.DEFAULT_CURRENCY_FOR_LANG[lang]
    return settings.DEFAULT_CURRENCY_FOR_LANG[settings.LANGUAGE_CODE]


def format_price(price, currency, decimals=2):
    if currency not in settings.CURRENCY_FORMATS:
        raise Exception("Currency %s is not supported!" % currency)
    return settings.CURRENCY_FORMATS[currency].replace('2', str(decimals)).format(float(price)).replace('.', ',')


def get_local_domain():
    lang_code = get_language()
    lang_dict = {v: k for k, v in settings.SUBDOMAIN_LANGUAGES.items()}
    return "{}://{}.{}".format(settings.SITE_PROTOCOL, lang_dict[lang_code], settings.SITE_DOMAIN)
