from django.utils.translation import activate
from django.conf import settings

from plata.shop import notifications


class SendConfirmedHandler(notifications.EmailHandler):
    """
    Send an e-mail with attached invoice to the customer after successful
    order completion, optionally BCC'ing the addresses passed as
    ``always_bcc`` to the handler upon initialization.

    Usage::

        signals.order_paid.connect(
            SendConfirmedHandler(always_bcc=['owner@example.com']),
            weak=False)
    """

    def message(self, sender, order, **kwargs):
        if order.language_code:
            activate(order.language_code)

        message = self.create_email_message(
            'plata/notifications/%s/order_confirmed.txt' % order.language_code,
            order=order,
            bank_attrs=settings.PAYMENT_BANK_ATTRS,
            settings=settings,
            **kwargs)

        message.to.append(order.email)
        return message


class SendPaidHandler(notifications.EmailHandler):

    def message(self, sender, order, **kwargs):
        if order.language_code:
            activate(order.language_code)

        message = self.create_email_message(
            'plata/notifications/%s/order_paid.txt' % order.language_code,
            order=order,
            settings=settings,
            **kwargs)

        message.to.append(order.email)
        return message


