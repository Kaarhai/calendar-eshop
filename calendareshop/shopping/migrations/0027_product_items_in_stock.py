# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0026_product_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='items_in_stock',
            field=models.IntegerField(default=0),
        ),
    ]
