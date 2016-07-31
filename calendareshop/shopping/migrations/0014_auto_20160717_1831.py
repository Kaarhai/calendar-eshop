# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0013_customorder_shipping_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customorder',
            name='payment_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Payment price'),
        ),
        migrations.AddField(
            model_name='customorder',
            name='shipping_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Shipping price'),
        ),
    ]
