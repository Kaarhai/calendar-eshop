"""
Payment module for cash handling

Automatically completes every order passed.
"""

from __future__ import absolute_import, unicode_literals

import logging

from django.utils.translation import ugettext_lazy as _

from plata.payment.modules.cod import PaymentProcessor as CODPaymentProcessor


logger = logging.getLogger(__name__)


class PaymentProcessor(CODPaymentProcessor):
    key = 'cash'
    default_name = _('Cash')
