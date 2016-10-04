import datetime
import logging

from django.utils.translation import activate
from django.conf import settings

from plata.shop import notifications

from calendareshop.utils import get_local_domain

logger = logging.getLogger(__name__)


class HtmlEmailHandler(notifications.EmailHandler):

    def context(self, ctx, **kwargs):
        ctx = super(HtmlEmailHandler, self).context(ctx, **kwargs)
        ctx.update({
            'domain': get_local_domain(),
            'is_preorder': settings.PREORDER_END > datetime.date.today(),
            'bank_attrs': settings.PAYMENT_BANK_ATTRS,
        })
        return ctx

    def create_email_message(self, template_name, **kwargs):
        email = super(HtmlEmailHandler, self).create_email_message(template_name, **kwargs)
        email.content_subtype = 'html'
        return email


class SendConfirmedHandler(HtmlEmailHandler):
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
        # get CustomOrder instance
        from models import CustomOrder
        order = CustomOrder.objects.get(pk=order.pk)

        if order.language_code:
            activate(order.language_code)

        message = self.create_email_message(
            'plata/notifications/order_confirmed.html',
            order=order,
            is_preorder=settings.PREORDER_END > datetime.date.today(),
            bank_attrs=settings.PAYMENT_BANK_ATTRS,
            settings=settings,
            **kwargs)

        message.to.append(order.email)
        return message


class SendPaidHandler(HtmlEmailHandler):

    def message(self, sender, order, **kwargs):
        # get CustomOrder instance
        from models import CustomOrder
        order = CustomOrder.objects.get(pk=order.pk)

        if order.language_code:
            activate(order.language_code)

        message = self.create_email_message(
            'plata/notifications/order_paid.html',
            order=order,
            is_preorder=settings.PREORDER_END > datetime.date.today(),
            settings=settings,
            **kwargs)

        message.to.append(order.email)
        return message


