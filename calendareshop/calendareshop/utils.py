from django.conf import settings


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
