# -*- coding: utf-8 -*-
import logging
import re

from django.core.management.base import BaseCommand
from post_office import mail
from django.conf import settings

from shopping.models import CustomOrder, email_hash

logger = logging.getLogger(__name__)
settings.EMAIL_BACKEND = 'post_office.EmailBackend'


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--doit', dest='doit', action='store_true', default=False)
        parser.add_argument('--send-test', dest='send_test', action='store_true', default=False)

    def handle(self, *args, **options):
        doit = options['doit']
        send_test = options['send_test']

        qs = CustomOrder.objects.filter(personal_information_consent=True).values_list('email', 'language_code').distinct()
        if send_test:
            qs = [
                ('flaiming@gmail.com', 'cs')
            ]

        for email, lang in qs:
            if lang != 'cs':
                # we don't have translated consent, so just skip it
                continue

            text = """Pěkný den,

i tento rok budeme vydávat dračí kalendář od tvůrců z Draci.info.
V současné době naši členové pracují na obrázcích do kalendáře.
Držíme se stejného harmonogramu jako minulý rok, <b>předobjednávky otevřeme na přelomu září a října</b>. Kalendáře budeme následně rozesílat během listopadu.

Přejeme Vám pěkné léto a těšíme se na Vás na podzim s novým kalendářem!

Organizační tým projektů Draci.info"""
            if doit:
                logger.info('Sending email for %s:\n%s', email, text)
                mail.send(
                    [email],
                    'kalendar@draci.info',
                    template='default_%s' % lang,
                    context={
                        'domain': 'http://kalendar.draci.info',
                        'subject': 'Novinky ohledně kalendáře Draci.info',
                        'content_html': text.replace('\n', '<br />'),
                        'content_text': re.sub(r'<a href="([^"]*)"[^>]*>([^<]+)</a>', '\\2 \\1 ', text, flags=re.U),
                    },
                )


