# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0024_product_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
