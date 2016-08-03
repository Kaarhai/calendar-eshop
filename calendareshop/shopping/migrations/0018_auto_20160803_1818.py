# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '__first__'),
        ('shopping', '0017_payment_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingRegionPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currency', models.CharField(max_length=3, verbose_name='currency', choices=[(b'CZK', b'CZK'), (b'EUR', b'EUR'), (b'USD', b'USD')])),
                ('_unit_price', models.DecimalField(verbose_name='unit price', max_digits=18, decimal_places=10)),
                ('tax_included', models.BooleanField(default=True, help_text='Is tax included in given unit price?', verbose_name='tax included')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
                'verbose_name': 'price',
                'verbose_name_plural': 'prices',
            },
        ),
        migrations.AlterModelOptions(
            name='shippingregion',
            options={'ordering': ('shipping', 'region', 'quantity_min')},
        ),
        migrations.RemoveField(
            model_name='shippingregion',
            name='price',
        ),
        migrations.AddField(
            model_name='shippingregionprice',
            name='shipping_region',
            field=models.ForeignKey(related_name='shipping_region_prices', verbose_name='shipping region', to='shopping.ShippingRegion'),
        ),
        migrations.AddField(
            model_name='shippingregionprice',
            name='tax_class',
            field=models.ForeignKey(related_name='+', verbose_name='tax class', to='shop.TaxClass'),
        ),
    ]
