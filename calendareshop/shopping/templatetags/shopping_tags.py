# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)
import pdb as pdb_module
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.template import Node

from calendareshop.utils import get_currency_code, format_price as frmt_price

register = template.Library()


@register.simple_tag(takes_context=True)
def get_price(context, product):
    request = context['request']
    currency = get_currency_code(request)
    return frmt_price(product.get_price(currency).unit_price, currency, decimals=0)


@register.simple_tag
def format_price(price, currency):
    return frmt_price(price, currency)
