from django.contrib import admin

from django.utils.translation import ugettext_lazy as _

from plata.shop.admin import OrderAdmin
from modeltranslation.admin import TranslationAdmin

from . import models


class ProductPriceInline(admin.TabularInline):
    model = models.ProductPrice
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPriceInline]
    list_display = ('is_active', 'name', 'ordering')
    list_display_links = ('name',)
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

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
            'fields': ('notes', 'data'),
        }),
    )


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
