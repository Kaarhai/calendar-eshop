# -*- coding: utf-8 -*-
import json
import datetime
from collections import defaultdict

from django import forms
from django.contrib import messages
from django.contrib import auth, messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views import generic
from django.conf import settings
from django.conf.urls import url, patterns

from plata.contact.models import Contact
from plata.discount.models import Discount
from plata.shop.views import Shop, checkout_process_decorator, cart_not_empty, \
    order_already_confirmed, order_cart_validates

from .models import Product, CustomOrder, ShippingPayment, Payment, Shipping
from .forms import CustomCheckoutForm, CustomConfirmationForm, ShippingPaymentForm
from calendareshop.utils import get_currency_code


class CalendarShop(Shop):
    shipping_payment_template = "plata/shop_shipping_payment.html"

    def default_currency(self, request=None):
        """
        Return the default currency for instantiating new orders

        Override this with your own implementation if you have a
        multi-currency shop with auto-detection of currencies.
        """
        return get_currency_code(request)

    def order_from_request(self, request, create=False):
        order = super(CalendarShop, self).order_from_request(request, create)
        if order:
            # set custom order currency
            order.currency = get_currency_code(request)
            order.save()
        return order

    def get_urls(self):
        return super(CalendarShop, self).get_urls() + patterns('', self.get_shipping_payment_url())

    def get_shipping_payment_url(self):
        return url(r'^shipping-payment/$', checkout_process_decorator(
            cart_not_empty, order_already_confirmed, order_cart_validates,
        )(self.shipping_payment), name='plata_shop_shipping_payment')

    def checkout_form(self, request, order):
        return CustomCheckoutForm

    def checkout(self, request, order):
        """Handles the first step of the checkout process"""
        if not request.user.is_authenticated():
            if request.method == 'POST' and '_login' in request.POST:
                loginform = self.get_authentication_form(
                    data=request.POST,
                    prefix='login')

                if loginform.is_valid():
                    user = loginform.get_user()
                    auth.login(request, user)

                    order.user = user
                    order.save()

                    return HttpResponseRedirect('.')
            else:
                loginform = self.get_authentication_form(prefix='login')
        else:
            loginform = None

        if order.status < order.CHECKOUT:
            order.update_status(order.CHECKOUT, 'Checkout process started')

        OrderForm = self.checkout_form(request, order)

        orderform_kwargs = {
            'prefix': 'order',
            'instance': order,
            'request': request,
            'shop': self,
        }

        if request.method == 'POST' and '_checkout' in request.POST:
            orderform = OrderForm(request.POST, **orderform_kwargs)

            if orderform.is_valid():
                orderform.save()
                return self.redirect('plata_shop_shipping_payment')
        else:
            orderform = OrderForm(**orderform_kwargs)

        return self.render_checkout(request, {
            'order': order,
            'loginform': loginform,
            'orderform': orderform,
            'progress': 'checkout',
        })

    def render_checkout(self, request, context):
        """Renders the checkout page"""
        #context = self.get_context(request, context)
        return self.render(
            request,
            self.checkout_template,
            context
        )

    def shipping_payment(self, request, order):
        """
        Handles the order shipping and payment module selection step

        Hands off processing to confirmation
        """

        kwargs = {
            'order': order,
            'request': request,
            'shop': self,
        }

        if request.method == 'POST':
            form = ShippingPaymentForm(request.POST, **kwargs)

            if form.is_valid():
                form.save()
                return self.redirect('plata_shop_confirmation')
        else:
            form = ShippingPaymentForm(**kwargs)

        if order.status <= order.CHECKOUT:
            order.update_status(order.CHECKOUT, 'Shipping & Payment process started')

        selected_shipping = int(request.POST.get('shipping_type', order.shipping_type.pk if order.shipping_type else 0))
        selected_payment = int(request.POST.get('payment_type', order.payment_type.pk if order.payment_type else 0))

        # prepare dict with combinations of Shipping - Payment for use in template
        shipping_payment = defaultdict(dict)
        for ship_pay in ShippingPayment.objects.select_related('shipping', 'payment'):
            # if pre-order, do not use cash payment
            if settings.PREORDER_END > datetime.date.today() and ship_pay.payment.module == 'cash':
                continue
            shipping_payment[ship_pay.shipping.id]['price'] = ship_pay.shipping.get_shipping_price(
                quantity=order.total_quantity,
                currency=order.currency,
                country_code=order.billing_country
            )
            shipping_payment[ship_pay.shipping.id].setdefault('payment', [])
            shipping_payment[ship_pay.shipping.id]['payment'].append(ship_pay.payment.id)

        return self.render_shipping_payment(request, {
            'order': order,
            'form': form,
            'shipping_payment_json': json.dumps(shipping_payment),
            'shipping_payment': dict(shipping_payment),
            'payment_payment': {p.pk: (p.get_payment_price(order), p.module) for p in Payment.objects.all()},
            'all_payment_ids_json': json.dumps(list(Payment.objects.values_list('id', flat=True))),
            'progress': 'shipping_payment',
            'selected_shipping': selected_shipping,
            'selected_payment': selected_payment,
        })

    def render_shipping_payment(self, request, context):
        """Renders the shipping_payment page"""
        return self.render(
            request,
            self.shipping_payment_template,
            self.get_context(request, context)
        )

    def confirmation_form(self, request, order):
        return CustomConfirmationForm

shop = CalendarShop(Contact, CustomOrder, Discount)


product_list = generic.ListView.as_view(
    queryset=Product.objects.filter(is_active=True),
    template_name='product/product_list.html',
)


class OrderItemForm(forms.Form):
    quantity = forms.IntegerField(
        label=_('quantity'),
        initial=1,
        min_value=1,
        max_value=100
    )


def product_detail(request, object_id):
    product = get_object_or_404(Product.objects.filter(is_active=True), pk=object_id)

    if request.method == 'POST':
        form = OrderItemForm(request.POST)

        if form.is_valid():
            order = shop.order_from_request(request, create=True)
            try:
                order.modify_item(product, form.cleaned_data.get('quantity'))
                messages.success(request, _('The cart has been updated.'))
            except ValidationError, e:
                if e.code == 'order_sealed':
                    [messages.error(request, msg) for msg in e.messages]
                else:
                    raise

            return redirect('plata_shop_cart')
    else:
        form = OrderItemForm()

    return render_to_response('product/product_detail.html', {
        'object': product,
        'form': form,
    }, context_instance=RequestContext(request))


# TODO uncomment after deployment!!!
#@staff_member_required
def email_test(request, order_id, template):
    order = get_object_or_404(CustomOrder, pk=order_id)
    # overrides
    shipping = request.GET.get('shipping', None)
    if shipping:
        order.shipping_type = get_object_or_404(Shipping, code=shipping)
    payment = request.GET.get('payment', None)
    if payment:
        order.payment_type = get_object_or_404(Payment, module=payment)
    return render_to_response('plata/notifications/%s.html' % template, {
        'order': order,
        'bank_attrs': settings.PAYMENT_BANK_ATTRS,
    }, context_instance=RequestContext(request))
