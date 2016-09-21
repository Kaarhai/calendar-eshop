import logging
logger = logging.getLogger(__name__)

from django.utils import translation
from django.utils.cache import patch_vary_headers
from django.conf import settings

from .utils import get_currency_code


class SubdomainLanguageMiddleware(object):
    """
    Set the language for the site based on the subdomain the request
    is being served on. For example, serving on 'fr.domain.com' would
    make the language French (fr).
    """

    def process_request(self, request):
        host = request.get_host().split('.')

        lang = request.GET.get('lang', None)
        if lang in dict(settings.LANGUAGES):
            # set language by GET param
            translation.activate(lang)
            request.LANGUAGE_CODE = lang
        elif host and host[0] in settings.SUBDOMAIN_LANGUAGES:
            # set language based on subdomain
            lang = settings.SUBDOMAIN_LANGUAGES[host[0]]
            #logging.debug("Choosing language: {0}".format(lang))
            translation.activate(lang)
            request.LANGUAGE_CODE = lang

        # set currency
        currency = request.GET.get('currency', None)
        if currency and currency in settings.CURRENCIES:
            request.session[settings.CURRENCY_SESSION_KEY] = currency
        else:
            request.session[settings.CURRENCY_SESSION_KEY] = get_currency_code(request)

    def process_response(self, request, response):
        response.set_cookie(settings.CURRENCY_SESSION_KEY, get_currency_code(request))
        return response


#class CacheCurrencyMiddleware(object):
#
#    def process_request(self, request):
#        request.META['HTTP_X_CURRENCY'] = get_currency_code(request) or 'UNKNOWN'
#
#    def process_response(self, request, response):
#        if 'X-Currency' not in response:
#            response['X-Currency'] = get_currency_code(request) or 'UNKNOWN'
#
#        patch_vary_headers(response, ['X-Currency'])
#        return response

