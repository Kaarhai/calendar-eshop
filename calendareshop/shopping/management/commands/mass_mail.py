# -*- coding: utf-8 -*-
import logging
import re
import datetime

from django.core.management.base import BaseCommand
from post_office import mail
from django.conf import settings

from calendareshop.models import NewsletterSubscription
from shopping.models import CustomOrder, email_hash

logger = logging.getLogger(__name__)
settings.EMAIL_BACKEND = 'post_office.EmailBackend'


email_footer = u'<span style="color: #888;">Pokud si nepřejete tyto emaily nadále odebírat, odpovězte na tento email a do těla zprávy napište "odhlásit".</span><br>'


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--doit', dest='doit', action='store_true', default=False)
        parser.add_argument('--send-test', dest='send_test', action='store_true', default=False)

    def handle(self, *args, **options):
        doit = options['doit']
        send_test = options['send_test']

        year = datetime.datetime.today().year + 1

        sent_emails = set()
        #with open('member_mails.txt', 'r') as f:
        #    sent_emails = set(map(lambda x: x.strip(), f.readlines()))

        #emails = sent_emails
        emails = set()
        emails.update(list(CustomOrder.objects.filter(personal_information_consent=True, language_code='cs').values_list('email', flat=True)))
        emails.update(list(NewsletterSubscription.objects.values_list('email', flat=True)))
        emails = emails - sent_emails
        count = len(emails)
        print emails
        print count
        if send_test:
            emails = [
                'flaiming@gmail.com',
                'kitty@draci.info',
                #'exander77@gmail.com',
            ]
        else:
            logger.info('Total of emails that will be send: %s', count)

        email_pre_preorder = (
            u"Připravujeme předobjednávky kalendáře Draci.info %s" % year,
            u"""Pěkný den,

i tento rok budeme vydávat dračí kalendář od tvůrců z <a href="https://draci.info">Draci.info</a>.
V současné době naši členové čile pracují na obrázcích do kalendáře.
Držíme se stejného harmonogramu jako minulý rok, <b>předobjednávky otevřeme na přelomu září a října</b>. Kalendáře budeme následně rozesílat během listopadu.

Přejeme Vám pěkné léto a těšíme se na Vás na podzim s novým kalendářem!

Organizační tým projektů Draci.info""")

        email_preorder = (
            u"Předobjednávka kalendáře Draci.info %s otevřena" % year,
            u"""Pěkný den,

zahájili jsme <a href="https://kalendar.draci.info/">předobjednávky kalendáře Draci.info {year}</a>!
I letos se můžete těšit na 13 dračích obrázků od autorů z <a href="https://draci.info" target="_blank">Draci.info</a>.
Hotové kalendáře budeme rozesílat koncem listopadu.

Letos poprvé připravujeme i stolní kalendář, který bude možné předobjednat asi za týden. Budeme Vás o tom informovat emailem. Prosíme o trpělivost :)

Organizační tým projektů Draci.info""".format(year=year))

        email_members = (
            u"Předobjednávky kalendářů %s otevřeny" % year,
            u"""Ahoj!

Jako členovi Draci.info Ti nabízíme kalendáře Draci.info, pexeso a omalovánky a speciální cenu.

<b>Jak objednat?</b>
1) Sečti ceny produktů, které si chceš objednat a připočti poštovné. (ceny viz níže)
2) Pošli platbu na <b>infácký účet 2901050776 / 2010</b> do zpráy pro příjemce napiš svou přezdívku na infu a obsah objednávky
3) Odpověz na tento email NEBO napiš Kitty vzkaz obsahující: info za co jsi zaplatil(a) + reálné jméno a adresa, nebo info o vyzvednutí na sletu

<b>Ceny</b>
Nástěnný kalendář {year}: 140 Kč/ks
Stolní kalendář {year}: 180 Kč/ks *
Pexeso: 15 Kč **
Omalovánky: 170 Kč ***

<b>Poštové</b>
Poštovné za 1 kalendář po ČR = 80 Kč
Poštovné za 2-4 kalendáře po ČR = 90 Kč
Poštovné za 1 kalendář do SK = 190 Kč
Poštovné za 2 kalendáře do SK = 270 Kč
Poštovné za 3-4 kalendáře do SK = 410 Kč
* Ke každému ks nástěnného kalendáře můžeš objednat 1ks stolního bez navýšení poštovného -> za každý ks stolního nad to navíc si připočti 40 Kč. Poštovné za jeden samostatný stolní kalendář je 60 Kč.
** Pexeso poštou lze pouze s kalednářem.
*** 1 ks omalovánek nenavyšuje cenu poštovného

Příklad: Objednávám 1 nástěnný, 2 stolní, 1 omalovánku a 1 pexeso. Za poštovné zaplatím 80 + 40 = 120 Kč. Za produkty 140 + 2x180 + 170 + 15 = 685 Kč. Celkem pošlu na účet 805 Kč.
(Pokud si nebudeš vědět rady s výpočtem poštovného, napiš Kitty)

<b>Kalendáře budou rozesílány/rozdávány v listopadu/prosinci.</b>

<b>Autoři</b>
Každý autor má nárok na 1 kus kalendáře zdarma a to včetně poštovného na celou objednávku.
Pro stolní platí to samé, pokud v něm má autor alespoň 2 obrázky.
Autor si může vybrat, jestli chce stolní nebo nástěnný kalendář.

Těšíme se na tvou objednávku!

Organizační tým projektů Draci.info""".format(year=year))


        email_members2 = (
        u"Předobjednávky kalendáře končí v úterý!",
        u"""
Ahoj!
Pokud ještě váháš s objednávkou kalendáře, je nejvyšší čas se rozhoupat!<br>
<b>Předobjednávky přijímáme do úterý 23.10.2018</b> - nejpozději tento den musí být platba připsána na účet Draci.info.<br>
Máš-li již objednáno a zaplaceno, omlouváme se za spam a děkujeme :D

Do zásoby nakoupíme jen velmi malé množství, není tedy dobrý nápad čekat déle a spoléhat se na to, že kalendáře ještě budou. Prodej ze skladových zásob navíc bude dražší.

Nezapomneň: letos máme také <b>stolní kalendář</b> :)

Pokud máš jakýkoli dotaz, nebo si chceš objednat, stačí odpovědět na tento email. Podrobné info k objednávkám najdeš buď na Draci.info v příslušném <a href="https://draci.info/index.php?cls=forum&id=153">fóru</a>, nebo v předchozím emailu.

Organizační tým projektů Draci.info""".format(year=year))

        email_table_calendar = (
            u"Předobjednávka stolního kalendáře Draci.info %s" % year,
            u"""Krásný podzimní den!

S radostí Vám oznamujeme, že tento rok poprvé nabízíme veřejnosti i <b>stolní dračí kalendář</b>!
Předobjednat si ho můžete v našem <a href="https://kalendar.draci.info/">eshopu</a> za 250 Kč.
Tisk i rozesílání proběhne společně s nástěnnými kalednáři koncem listopadu.

Pokud máte zájem o stolní i nástěnný kalendář, připravili jsme pro Vás <b>speciální balíček za výhodnou cenu</b>!
Vše najdete na eshopu.

<img src="https://kalendar.draci.info/static/img/stolni_kalendar_2019_1.jpg" style="width: 100%;" />
<img src="https://kalendar.draci.info/static/img/stolni_kalendar_2019_2.jpg" style="width: 100%;" />

Těšíme se na Vaše objednávky.

Organizační tým projektů Draci.info""".format(year=year))

        email_almost_sent = (
                u"Kalendáře Draci.info %s budou již brzy" % year,
            u"""Krásný den!

Omlouváme se za zpoždění, kalendáře jsou již zadané k tisku a začneme je rozesílat hned jak budou hotové, tedy v průběhu příštího týdne.
Zatím se můžete pokochat alespoň testovacími tisky:

<img src="https://kalendar.draci.info/static/img/kalendar2019_testovaci.jpg" style="width: 100%;" />

Máme pro Vás také jednu novinku - stolní dračí kalendář!

<img src="https://kalendar.draci.info/static/img/kalendar2019_stolni.jpg" style="width: 100%;" />

Mějte prosím trpělivost, do Vánoc vám kalendáře Draci.info určitě stihneme dodat :)

Organizační tým projektů Draci.info""".format(year=year))

        current_email = email_almost_sent
        subject = current_email[0]
        text = current_email[1]

        for email in emails:
            logger.info(u'Sending email for %s:\n%s', email, text)
            if doit:
                mail.send(
                    [email],
                    u'Kalendář Draci.info <kalendar@draci.info>',
                    template='default_cs',
                    context={
                        'domain': 'http://kalendar.draci.info',
                        'subject': subject,
                        'content_html': text.replace('\n', '<br />'),
                        'content_text': re.sub(r'<a href="([^"]*)"[^>]*>([^<]+)</a>', '\\2 \\1 ', re.sub('</?(?:b|small)>', '', text), flags=re.U),
                        'footer_text': email_footer,
                    },
                )


