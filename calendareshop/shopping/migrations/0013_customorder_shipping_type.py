# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0012_auto_20160717_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='customorder',
            name='shipping_type',
            field=models.ForeignKey(related_name='orders', default=1, to='shopping.Shipping'),
            preserve_default=False,
        ),
    ]
