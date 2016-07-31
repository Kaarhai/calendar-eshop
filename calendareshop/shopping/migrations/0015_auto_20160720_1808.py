# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0014_auto_20160717_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customorder',
            name='payment_type',
            field=models.ForeignKey(related_name='orders', to='shopping.Payment', null=True),
        ),
        migrations.AlterField(
            model_name='customorder',
            name='shipping_type',
            field=models.ForeignKey(related_name='orders', to='shopping.Shipping', null=True),
        ),
    ]
