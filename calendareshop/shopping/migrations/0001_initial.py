# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0004_auto_20150918_1832'),
        ('shop', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currency', models.CharField(max_length=3, verbose_name='currency', choices=[(b'CZK', b'CZK'), (b'EUR', b'EUR'), (b'USD', b'USD')])),
                ('_unit_price', models.DecimalField(verbose_name='unit price', max_digits=18, decimal_places=10)),
                ('tax_included', models.BooleanField(default=True, help_text='Is tax included in given unit price?', verbose_name='tax included')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('ordering', models.PositiveIntegerField(default=0, verbose_name='ordering')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('project', models.ForeignKey(related_name='products', to='calendareshop.Project')),
                ('tax_class', models.ForeignKey(related_name='+', verbose_name='tax class', to='shop.TaxClass')),
            ],
            options={
                'ordering': ['ordering', 'name'],
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
