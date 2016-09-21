from modeltranslation.translator import translator, TranslationOptions

from models import Shipping, Payment, Product


class ShippingTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Shipping, ShippingTranslationOptions)


class PaymentTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Payment, PaymentTranslationOptions)

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Product, ProductTranslationOptions)
