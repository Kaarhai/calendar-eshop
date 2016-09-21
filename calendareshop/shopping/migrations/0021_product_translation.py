# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0020_auto_20160805_0955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('name',), 'verbose_name': 'country', 'verbose_name_plural': 'countries'},
        ),
        migrations.AlterModelOptions(
            name='customorder',
            options={'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'payment', 'verbose_name_plural': 'payments'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'region', 'verbose_name_plural': 'regions'},
        ),
        migrations.AlterModelOptions(
            name='shipping',
            options={'verbose_name': 'shipping', 'verbose_name_plural': 'shippings'},
        ),
        migrations.AlterModelOptions(
            name='shippingpayment',
            options={'verbose_name': 'shipping payment', 'verbose_name_plural': 'shipping payments'},
        ),
        migrations.AlterModelOptions(
            name='shippingregion',
            options={'ordering': ('shipping', 'region', 'quantity_min'), 'verbose_name': 'shipping region', 'verbose_name_plural': 'shipping regions'},
        ),
        migrations.AlterModelOptions(
            name='shippingregionprice',
            options={'verbose_name': 'shipping price for region', 'verbose_name_plural': 'shipping prices for region'},
        ),
        migrations.AddField(
            model_name='product',
            name='description_cs',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_cs',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.RunSQL("UPDATE shopping_product SET name_cs=name, name_en=name;", migrations.RunSQL.noop)
    ]
