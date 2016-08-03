from modeltranslation.translator import translator, TranslationOptions

from models import Shipping, Payment


class ShippingTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Shipping, ShippingTranslationOptions)


class PaymentTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Payment, PaymentTranslationOptions)
