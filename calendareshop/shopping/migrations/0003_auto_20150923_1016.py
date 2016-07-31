# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '__first__'),
        ('shopping', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currency', models.CharField(max_length=3, verbose_name='currency', choices=[(b'CZK', b'CZK'), (b'EUR', b'EUR'), (b'USD', b'USD')])),
                ('_unit_price', models.DecimalField(verbose_name='unit price', max_digits=18, decimal_places=10)),
                ('tax_included', models.BooleanField(default=True, help_text='Is tax included in given unit price?', verbose_name='tax included')),
            ],
            options={
                'ordering': ['-id'],
                'get_latest_by': 'id',
                'verbose_name': 'price',
                'verbose_name_plural': 'prices',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='_unit_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tax_class',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tax_included',
        ),
        migrations.AddField(
            model_name='productprice',
            name='product',
            field=models.ForeignKey(related_name='prices', verbose_name='product', to='shopping.Product'),
        ),
        migrations.AddField(
            model_name='productprice',
            name='tax_class',
            field=models.ForeignKey(related_name='+', verbose_name='tax class', to='shop.TaxClass'),
        ),
    ]
