# -*- coding: utf-8 -*-
import logging
import math
from decimal import Decimal

from django.core.management.base import BaseCommand

from shopping.models import Region, Country, ShippingRegionPrice, ShippingRegion

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--eur', nargs='+', type=float, dest='eur', required=True)
        parser.add_argument('--usd', nargs='+', type=float, dest='usd', required=True)

    def handle(self, *args, **options):
        for shipreg in ShippingRegion.objects.all():
            prices = {val.currency: val for val in shipreg.shipping_region_prices.all()}
            # recalculate EUR and USD prices
            czk = int(prices['CZK'].unit_price)

            eur = int(math.ceil(czk / options['eur'][0]))
            if eur != int(prices['EUR'].unit_price):
                logger.info("Changing EUR price from %s to %s", int(prices['EUR'].unit_price), eur)
                prices['EUR']._unit_price = Decimal(eur)
                prices['EUR'].save()

            usd = int(math.ceil(czk / options['usd'][0]))
            if usd != int(prices['USD'].unit_price):
                logger.info("Changing USD price from %s to %s", int(prices['USD'].unit_price), usd)
                prices['USD']._unit_price = Decimal(usd)
                prices['USD'].save()





