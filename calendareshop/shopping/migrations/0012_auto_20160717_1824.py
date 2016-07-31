# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0011_auto_20160716_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customorder',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='customorder',
            name='payment_price',
        ),
        migrations.RemoveField(
            model_name='customorder',
            name='shipping_price',
        ),
        migrations.RemoveField(
            model_name='customorder',
            name='shipping_type',
        ),
        migrations.AddField(
            model_name='customorder',
            name='payment_type',
            field=models.ForeignKey(related_name='orders', default=1, to='shopping.Payment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customorder',
            name='payment_cost',
            field=models.DecimalField(null=True, verbose_name='payment cost', max_digits=18, decimal_places=10, blank=True),
        ),
        migrations.AlterField(
            model_name='customorder',
            name='payment_tax',
            field=models.DecimalField(default=Decimal('0.00'), verbose_name='payment tax', max_digits=18, decimal_places=10),
        ),
    ]
