# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)
from django import template
from django.core.urlresolvers import resolve, Resolver404
from django.utils import translation

register = template.Library()


#@register.simple_tag(takes_context=True)
#def other_language_url(context, **kwargs):
#    lang = translation.get_language()
#    request = context['request']
#    try:
#        url_name = resolve(request.path_info).url_name
#    except Resolver404:
#        logger.error("URL '%s' cannot be resolved!", request.path_info)
#        return ""



