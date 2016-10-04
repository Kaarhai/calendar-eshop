import datetime

from django.contrib import admin

from django.utils.translation import ugettext_lazy as _

from plata.shop.admin import OrderAdmin, OrderPaymentAdmin, OrderItemInline, OrderStatusInline
from plata.shop import signals
from plata.shop import models as plata_models
from modeltranslation.admin import TranslationAdmin

from . import models


class ProductPriceInline(admin.TabularInline):
    model = models.ProductPrice
    extra = 0


class ProductAdmin(TranslationAdmin):
    inlines = [ProductPriceInline]
    list_display = ('is_active', 'name', 'ordering')
    list_display_links = ('name',)
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    filter_horizontal = ('projects',)

admin.site.register(models.Product, ProductAdmin)


class CustomOrderAdmin(OrderAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'created', 'confirmed', 'user', 'email',
                'language_code', 'status'),
        }),
        (_('Billing address'), {
            'fields': models.Order.address_fields('billing_'),
        }),
        (_('Shipping address'), {
            'fields': (
                ['shipping_same_as_billing']
                + models.Order.address_fields('shipping_')),
        }),
        (_('Order items'), {
            'fields': ('items_subtotal', 'items_discount', 'items_tax'),
        }),
        (_('Shipping'), {
            'fields': ('shipping_cost', 'shipping_discount', 'shipping_tax', 'shipping_type'),
        }),
        (_('Payment'), {
            'fields': ('payment_cost', 'payment_tax', 'payment_type'),
        }),
        (_('Total'), {
            'fields': ('currency', 'total', 'paid'),
        }),
        (_('Additional fields'), {
            'fields': ('notes', ),
        }),
    )
    inlines = [OrderItemInline, OrderStatusInline]
    list_display = (
        'admin_order_id', 'created', 'full_name', 'status', 'total',
        'balance_remaining', 'admin_is_paid', 'shipping_type', 'payment_type', 'additional_info')
    list_filter = ('status', 'shipping_type', 'payment_type')

    def get_queryset(self, request):
        qs = super(CustomOrderAdmin, self).get_queryset(request)
        if 'status__exact' not in request.GET:
            qs = qs.filter(status__gte=models.CustomOrder.CONFIRMED)
        return qs

    def full_name(self, obj):
        return "%s %s" % (obj.billing_first_name, obj.billing_last_name)

admin.site.register(models.CustomOrder, CustomOrderAdmin)


admin.site.register(models.Region)
admin.site.register(models.Country)


class ShippingAdmin(TranslationAdmin):
    pass

admin.site.register(models.Shipping, ShippingAdmin)


class PaymentAdmin(TranslationAdmin):
    pass

admin.site.register(models.Payment, PaymentAdmin)


class ShippingPaymentAdmin(admin.ModelAdmin):
    list_filter = ('shipping', 'payment')

admin.site.register(models.ShippingPayment, ShippingPaymentAdmin)


class ShippingRegionPriceInline(admin.TabularInline):
    model = models.ShippingRegionPrice
    extra = 0


class ShippingRegionAdmin(admin.ModelAdmin):
    inlines = [ShippingRegionPriceInline]
    list_filter = ('shipping', 'region')


admin.site.register(models.ShippingRegion, ShippingRegionAdmin)


# TODO make django adminaction to confirm payment, move logic to OrderPayment model
#def confirm_payment(modeladmin, request, queryset):
#    for item in queryset:
#        item.


class CustomOrderPaymentAdmin(OrderPaymentAdmin):

    def save_form(self, request, form, *args, **kwargs):
        # store old status value
        old_status = None
        if form.instance.pk:
            old_status = plata_models.OrderPayment.objects.get(pk=form.instance.pk).status

        obj = super(CustomOrderPaymentAdmin, self).save_form(request, form, *args, **kwargs)

        # test if payment has been authorized
        if old_status != obj.status and obj.status == plata_models.OrderPayment.AUTHORIZED:
            obj.authorized = datetime.datetime.now()
            # payment has been paid --> send order_paid signal
            signals.order_paid.send(
                sender=obj,
                order=obj.order,
                payment=obj,
                request=request
            )
            # create new OrderStatus(status=PAID) if not already created
            if not obj.order.statuses.filter(status__gte=models.CustomOrder.PAID).exists():
                status = plata_models.OrderStatus(order=obj.order, status=models.CustomOrder.PAID)
                status.save()

        return obj


admin.site.unregister(plata_models.Order)
admin.site.unregister(plata_models.OrderPayment)
admin.site.register(plata_models.OrderPayment, CustomOrderPaymentAdmin)
