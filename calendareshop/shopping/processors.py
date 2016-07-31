from decimal import Decimal

from django.conf import settings

from plata.shop.processors import ProcessorBase


class ShippingProcessor(ProcessorBase):
    """
    TODO
    """

    def process(self, order, items):
        if order.shipping_type:
            cost = Decimal(order.total_shipping_price)
        else:
            cost = Decimal('0.00')
        tax = settings.TAX

        order.shipping_cost, __ = self.split_cost(cost, tax)
        order.shipping_discount = min(
            order.discount_remaining,
            order.shipping_cost,
        )
        order.shipping_tax = tax / 100 * (
            order.shipping_cost - order.shipping_discount)

        self.set_processor_value(
            'total', 'shipping',
            order.shipping_cost - order.shipping_discount
            + order.shipping_tax)

        tax_details = dict(order.data.get('tax_details', []))
        self.add_tax_details(
            tax_details, tax, order.shipping_cost,
            order.shipping_discount, order.shipping_tax)
        order.data['tax_details'] = list(tax_details.items())


class PaymentProcessor(ProcessorBase):
    """
    TODO
    """

    def process(self, order, items):
        if order.shipping_type:
            cost = Decimal(order.total_payment_price)
        else:
            cost = Decimal('0.00')
        tax = settings.TAX

        order.payment_cost, __ = self.split_cost(cost, tax)
        order.payment_tax = tax / 100 * (
            order.payment_cost)

        self.set_processor_value(
            'total', 'payment',
            order.payment_cost
            + order.payment_tax)

        tax_details = dict(order.data.get('tax_details', []))
        self.add_tax_details(
            tax_details, tax, order.payment_cost,
            None, order.payment_tax)
        order.data['tax_details'] = list(tax_details.items())

