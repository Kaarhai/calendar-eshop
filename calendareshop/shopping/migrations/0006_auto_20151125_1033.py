# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20151125_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='customorder',
            name='payment_cost',
            field=models.DecimalField(null=True, verbose_name='shipping cost', max_digits=18, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='customorder',
            name='payment_tax',
            field=models.DecimalField(default=Decimal('0.00'), verbose_name='shipping tax', max_digits=18, decimal_places=10),
        ),
    ]
