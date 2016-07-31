# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from plata.contact.forms import CheckoutForm
from plata.shop import signals

from django_countries.fields import LazyTypedChoiceField

from .models import CustomOrder, Shipping, Payment, Region, Country


class CustomCheckoutForm(CheckoutForm):
    class Meta:
        fields = ['email', 'shipping_same_as_billing']
        fields.extend('billing_%s' % f for f in CustomOrder.ADDRESS_FIELDS)
        fields.extend('shipping_%s' % f for f in CustomOrder.ADDRESS_FIELDS)
        model = CustomOrder

    billing_address = forms.CharField(label=_('address'), required=True)
    shipping_address = forms.CharField(label=_('address'), required=False)
    # override it so it will be required
    billing_country = LazyTypedChoiceField(choices=Country.objects.values_list('code', 'name'), required=True)

    def clean(self):
        data = super(CustomCheckoutForm, self).clean()

        if not data.get('shipping_same_as_billing'):
            for f in self.REQUIRED_ADDRESS_FIELDS:
                field = 'shipping_%s' % f
                if not data.get(field):
                    self._errors[field] = self.error_class([
                        _('This field is required.')])

        return data


class ShippingPaymentForm(forms.Form):
    class Meta:
        fields = ['notes', 'shipping_type',
                  'payment_type', 'terms_and_conditions']

    notes = forms.CharField(label=_('notes'), required=False, widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    terms_and_conditions = forms.BooleanField(
        label=_('I accept the terms and conditions.'),
        required=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.shop = kwargs.pop('shop')
        self.order = kwargs.pop('order')
        super(ShippingPaymentForm, self).__init__(*args, **kwargs)
        self.payment_modules = self.shop.get_payment_modules(self.request)

        # TODO sanitize possible exceptions
        # set shipping types based on region
        total_quantity = self.order.total_quantity
        region = Region.objects.filter(countries__code=self.order.billing_country.code)
        shippings = Shipping.objects.filter(shipregions__region=region, shipregions__quantity_min__lte=total_quantity, shipregions__quantity_max__gte=total_quantity)
        self.fields['shipping_type'] = forms.ChoiceField(
            choices=shippings.values_list('id', 'name'),
            widget=forms.RadioSelect(attrs={'settings': settings}),
            required=True
        )
        payments = set()
        for shipping in shippings:
            payments.update(shipping.payments.all())
        self.fields['payment_type'] = forms.ChoiceField(
            choices=[(payment.id, payment.name) for payment in payments],
            widget=forms.RadioSelect(attrs={'settings': settings}),
            required=True
        )

    def clean(self):
        data = super(ShippingPaymentForm, self).clean()
        self.order.validate(self.order.VALIDATE_ALL)

        shipping_type_id = data.get('shipping_type', None)
        data['shipping_type'] = Shipping.objects.filter(pk=shipping_type_id).first()

        payment_type_id = data.get('payment_type', None)
        data['payment_type'] = Payment.objects.filter(pk=payment_type_id).first()

        return data

    def save(self):
        if 'shipping_type' in self.cleaned_data:
            self.order.shipping_type = self.cleaned_data['shipping_type']
        if 'payment_type' in self.cleaned_data:
            self.order.payment_type = self.cleaned_data['payment_type']
        self.order.save()


class CustomConfirmationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.order = kwargs.pop('order')
        self.request = kwargs.pop('request')
        self.shop = kwargs.pop('shop')
        self.payment_modules = self.shop.get_payment_modules(self.request)
        super(CustomConfirmationForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = super(CustomConfirmationForm, self).clean()
        self.order.validate(self.order.VALIDATE_ALL)
        return data

    def process_confirmation(self):
        """
        Process the successful order submission
        """
        self.order.update_status(self.order.CONFIRMED, 'Confirmation given')
        signals.order_confirmed.send(
            sender=self.shop,
            order=self.order,
            request=self.request)

        module = dict(
            (m.key, m) for m in self.payment_modules
        )[self.order.payment_type.module]

        return module.process_order_confirmed(self.request, self.order)
