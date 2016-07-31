# -*- coding: utf-8 -*-
import requests
import logging
logger = logging.getLogger(__name__)

from django.core.management.base import BaseCommand

from shopping.models import Region, Country


class Command(BaseCommand):

    def handle(self, *args, **options):
        resp = requests.get('http://restcountries.eu/rest/v1/region/europe', verify=False)
        data = resp.json()

        region = Region.objects.get(code='eu')
        for d in data:
            code = d['alpha2Code']
            try:
                country = Country.objects.get(code=code)
                country.region = region
                country.save()
            except Country.DoesNotExist:
                print "%s skipped!" % d['name']


