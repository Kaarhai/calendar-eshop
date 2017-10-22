# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0025_payment_shipping_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_main',
            field=models.BooleanField(default=True, verbose_name='is main product'),
        ),
    ]
