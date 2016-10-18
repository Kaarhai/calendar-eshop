"""
Payment module for bank transfer handling

Needs manual approval of ammount received
"""

from __future__ import absolute_import, unicode_literals

import logging

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

import plata
from plata.payment.modules.base import ProcessorBase
from plata.shop.models import OrderPayment


logger = logging.getLogger(__name__)


class PaymentProcessor(ProcessorBase):
    key = 'bank'
    default_name = _('Bank transfer')

    def process_order_confirmed(self, request, order):
        if not order.balance_remaining:
            return self.already_paid(order)

        logger.info('Processing order %s using BANK' % order)

        payment = self.create_pending_payment(order)

        payment.status = OrderPayment.PROCESSED
        payment.save()

        if plata.settings.PLATA_STOCK_TRACKING:
            StockTransaction = plata.stock_model()
            self.create_transactions(
                order, _('payment process reservation'),
                type=StockTransaction.PAYMENT_PROCESS_RESERVATION,
                negative=True, payment=payment)

        order = order.reload()

        return self.shop.redirect('plata_order_success')

