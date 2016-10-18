# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0023_shipping_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='items_in_stock',
            field=models.IntegerField(default=0),
        ),
    ]
