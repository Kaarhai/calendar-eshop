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
        parser.add_argument('--test', dest='test', action='store_true')

    def handle(self, *args, **options):
        #test = options['test']

        for email, lang in CustomOrder.objects.filter(status__gte=CustomOrder.CONFIRMED, personal_information_consent=False).values_list('email', 'language_code').distinct():
            if lang != 'cs':
                # we don't have translated consent, so just skip it
                continue

            hash = email_hash(email)

            text = """Pěkný den,
jsme moc rádi, že podporujete náš projekt dračích kalendářů!
Aby to tak zůstalo, je potřeba, abychom od Vás měli na základě Obecného nařízení o ochraně osobních údajů (GDPR) Váš jednoznačný souhlas se zpracováním Vašich osobních údajů.

Pokud od nás chcete i nadále dostávat informace o nových produktech, slevových akcích a novinkách, potvrďte tento email tlačítkem níže. Tento souhlas bude dán na 20 let a je kdykoli odvolatelný.

<a href="{}" style="font-size: 150%;">ANO, souhlasím</a>

Pokud souhlas nepotvrdíte, přestanete od nás od 25. května dostávat veškeré novinky a všechny Vaše osobní údaje budou u nás vymazána (s výjimkou dat ze zákona požadovaných pro účetnictví).

Jaké Vaše osobní údaje zpracováváme? Jde o jméno, příjmení, adresu, e-mail a IP adresu. Nově máte právo na přístup, opravu a výmaz spravovaných osobních dat, dále právo být zapomenut, právo na omezení zpracování, přenositelnost údajů a v neposlední řadě právo vznést námitku.

Kompletní znění souhlasu se zpracováním osobních údajů najdete <a href="https://kalendar.draci.info/souhlas-s-poskytnutim-osobnich-udaju/">na našem webu</a>.

Nechť Vás draci provází!

Organizační tým projektů Draci.info""".format("https://kalendar.draci.info/gdpr_consent/?email=%s&hash=%s" % (email, hash))
            logger.info('Preparing email for %s', email)
            mail.send(
                [email],
                'kalendar@draci.info',
                template='default_%s' % lang,
                context={
                    'domain': 'http://kalendar.draci.info',
                    'subject': 'Kalendář Draci.info - souhlas s poskytnutím osobních údajů',
                    'content_html': text.replace('\n', '<br />'),
                    'content_text': re.sub(r'<a href="([^"]*)"[^>]*>([^<]+)</a>', '\\2 \\1 ', text, flags=re.U),
                },
            )

