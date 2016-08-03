# -*- coding: utf-8 -*-
from collections import OrderedDict
from decimal import Decimal
import logging
logger = logging.getLogger(__name__)

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from plata.product.models import ProductBase
from plata.shop.models import PriceBase, Order
from calendareshop.models import Project
from .notifications import SendConfirmedHandler

from plata.shop import notifications, signals as shop_signals


#shop_signals.contact_created.connect(
#    notifications.ContactCreatedHandler(always_bcc=[]),
#    weak=False)
shop_signals.order_confirmed.connect(
    SendConfirmedHandler(always_bcc=[]),
    weak=False)
shop_signals.order_paid.connect(
    notifications.SendInvoiceHandler(always_bcc=[]),
    weak=False)
shop_signals.order_paid.connect(
    notifications.SendPackingSlipHandler(
        always_to=[],
        always_bcc=[]),
    weak=False)


class CustomOrder(Order):
    #: Order object is a cart.
    CART = 10
    #: Checkout process has started.
    CHECKOUT = 20
    #: Order has been confirmed, but it not (completely) paid for yet.
    CONFIRMED = 30
    #: Order has been completely paid for.
    PAID = 40
    #: Order has been completed. Plata itself never sets this state,
    #: it is only meant for use by the shop owners.
    COMPLETED = 50

    shipping_type = models.ForeignKey('Shipping', related_name='orders', null=True, blank=True)
    payment_type = models.ForeignKey('Payment', related_name='orders', null=True, blank=True)

    shipping_price = models.PositiveIntegerField(_('Shipping price'), default=0)
    payment_price = models.PositiveIntegerField(_('Payment price'), default=0)

    payment_cost = models.DecimalField(
        _('payment cost'),
        max_digits=18, decimal_places=10, blank=True, null=True)
    payment_tax = models.DecimalField(
        _('payment tax'),
        max_digits=18, decimal_places=10, default=Decimal('0.00'))

    @property
    def total_quantity(self):
        return sum([i.quantity for i in self.items.all()])

    @property
    def total_shipping_price(self):
        if self.shipping_type:
            return self.shipping_type.get_shipping_price(self.billing_country, self.total_quantity, self.currency)
        return 0

    @property
    def total_payment_price(self):
        if self.payment_type:
            return self.payment_type.get_payment_price(self.billing_country, self.total_quantity)
        return 0

    @property
    def payment(self):
        """
        Returns the payment cost, with or without tax depending on this
        order's ``price_includes_tax`` field.
        """
        if self.price_includes_tax:
            if self.payment_cost is None:
                return None

            return (
                self.payment_cost
                + self.payment_tax)
        else:
            logger.error(
                'Payment calculation with'
                ' PLATA_PRICE_INCLUDES_TAX=False is not implemented yet')
            raise NotImplementedError


class Product(ProductBase):
    is_active = models.BooleanField(_('is active'), default=True)
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
    ordering = models.PositiveIntegerField(_('ordering'), default=0)
    description = models.TextField(_('description'), blank=True)
    image = models.ImageField(upload_to="products/")

    project = models.ForeignKey(Project, related_name="products")

    class Meta:
        ordering = ['ordering', 'name']
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('plata_product_detail', (), {'object_id': self.pk})


class ProductPrice(PriceBase):
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='prices')

    class Meta:
        get_latest_by = 'id'
        ordering = ['-id']
        verbose_name = _('price')
        verbose_name_plural = _('prices')


class Payment(models.Model):
    module = models.CharField(_('module code'), choices=settings.PLATA_PAYMENT_MODULE_NAMES.items(), max_length=10)
    name = models.CharField(_('name'), max_length=50)

    def __unicode__(self):
        return self.name

    def get_payment_price(self, country_code, quantity):
        # TODO finish, return zero for now
        return 0


class Shipping(models.Model):
    name = models.CharField(_('name'), max_length=50)

    payments = models.ManyToManyField(Payment, related_name='shippings', through='ShippingPayment')

    def __unicode__(self):
        return self.name

    def get_shipping_price(self, country_code, quantity, currency):
        ship_reg = ShippingRegion.objects.filter(shipping=self, quantity_min__lte=quantity, quantity_max__gte=quantity, region__countries__code=country_code).first()
        if ship_reg:
            try:
                return int(ship_reg.shipping_region_prices.get(currency=currency).unit_price)
            except ShippingRegionPrice.DoesNotExist:
                raise LookupError("Price for country %s, shipping %s, quantity %s and currency %s is missing, add it please!" % (country_code, self, quantity, currency))
        return 0


class Region(models.Model):
    code = models.CharField(_('code'), max_length=2, primary_key=True)
    name = models.CharField(_('name'), max_length=50)

    def __unicode__(self):
        return self.name

    def get_region_by_country_code(self, code):
        return Region.objects.filter(countries__code=code).first()


class Country(models.Model):
    code = models.CharField(_('code'), max_length=2, primary_key=True)
    name = models.CharField(_('name'), max_length=255, unique=True)
    region = models.ForeignKey(Region, related_name='countries', blank=True, null=True)

    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.code)

    @staticmethod
    def choices():
        uncategorized = []
        categorized = OrderedDict()
        for region in Region.objects.prefetch_related('countries'):
            if region.code == 'CZ':
                country = region.countries.first()
                uncategorized.append((country.pk, country.name))
            elif region.code == 'SK':
                country = region.countries.first()
                uncategorized.append((country.pk, country.name))
            else:
                categorized[region.name] = tuple(region.countries.values_list('pk', 'name'))
        return uncategorized + categorized.items()


class ShippingRegion(models.Model):
    quantity_min = models.PositiveIntegerField(_('min quantity'))
    quantity_max = models.PositiveIntegerField(_('max quantity'))

    shipping = models.ForeignKey(Shipping, related_name='shipregions')
    region = models.ForeignKey(Region, related_name='shipregions')

    class Meta:
        ordering = ('shipping', 'region', 'quantity_min')

    def __unicode__(self):
        return u"%s to %s with quantity %s" % (
            self.shipping,
            self.region,
            "%s-%s" % (self.quantity_min, self.quantity_max) if self.quantity_min != self.quantity_max else self.quantity_min,
        )


class ShippingRegionPrice(PriceBase):
    shipping_region = models.ForeignKey(ShippingRegion, verbose_name=_('shipping region'), related_name='shipping_region_prices')


class ShippingPayment(models.Model):
    price = models.PositiveIntegerField(_('price'), default=0)

    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s + %s (cena %s)" % (self.shipping, self.payment, self.price)
