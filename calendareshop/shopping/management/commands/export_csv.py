# -*- coding: utf-8 -*-
import logging
import csv
import datetime

from django.core.management.base import BaseCommand

from shopping.models import CustomOrder

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('order_export.csv', 'w') as f:
            writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            # write header
            writer.writerow(['id', 'paid', 'email', 'name', 'shipping_address', 'order'])
            # write rows
            for order in CustomOrder.objects.filter(status=CustomOrder.PAID, confirmed__year=datetime.date.today().year):
                paid = order.is_paid
                email = order.email
                name = "%s %s" % (order.billing_first_name, order.billing_last_name)
                shipping_address = order.addresses['shipping']
                items = "\n".join(order.items.all())
                row = [order.id, paid, email, name, shipping_address, items]
                writer.writerow(row)




