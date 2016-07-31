# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)
import pdb as pdb_module
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.template import Node

from calendareshop.utils import get_currency_code

register = template.Library()


@register.simple_tag(takes_context=True)
def get_price(context, product):
    request = context['request']
    currency = get_currency_code(request)
    return product.get_price(currency)


