from django.contrib.sites.models import Site

from models import ProjectType
from django.conf import settings

from .utils import get_currency_code


def project_types(request):
    return {
        'project_types': ProjectType.objects.all(),
        'calendars': ProjectType.objects.get(codename='calendar').projects.enabled()
    }


def site(request):
    site = Site.objects.get_current()
    language_subdomain = {y: x for x, y in settings.SUBDOMAIN_LANGUAGES.iteritems()}
    return {
        'site': site,
        'subdomain_languages': [(lang, "%s.%s" % (language_subdomain[lang], site.domain)) for lang, _ in settings.LANGUAGES],
        'currencies': settings.CURRENCIES,
        'selected_currency': get_currency_code(request)
    }


