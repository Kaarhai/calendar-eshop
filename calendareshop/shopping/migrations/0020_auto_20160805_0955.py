# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0019_auto_20160803_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingregionprice',
            name='shipping_region',
            field=models.ForeignKey(related_name='shipping_region_prices', verbose_name='shipping price', to='shopping.ShippingRegion'),
        ),
    ]
