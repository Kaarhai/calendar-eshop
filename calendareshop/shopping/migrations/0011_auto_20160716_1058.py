# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0010_auto_20160715_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='shippingregion',
            options={'ordering': ('shipping', 'region', 'quantity_min', 'price')},
        ),
    ]
