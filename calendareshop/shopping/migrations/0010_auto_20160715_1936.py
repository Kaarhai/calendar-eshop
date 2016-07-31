# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_auto_20151205_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=2, serialize=False, verbose_name='code', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('code', models.CharField(max_length=2, serialize=False, verbose_name='code', primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingPayment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price')),
                ('payment', models.ForeignKey(to='shopping.Payment')),
                ('shipping', models.ForeignKey(to='shopping.Shipping')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price')),
                ('quantity_min', models.PositiveIntegerField(verbose_name='min quantity')),
                ('quantity_max', models.PositiveIntegerField(verbose_name='max quantity')),
                ('region', models.ForeignKey(related_name='shipregions', to='shopping.Region')),
                ('shipping', models.ForeignKey(related_name='shipregions', to='shopping.Shipping')),
            ],
        ),
        migrations.AddField(
            model_name='shipping',
            name='payments',
            field=models.ManyToManyField(related_name='shippings', through='shopping.ShippingPayment', to='shopping.Payment'),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(related_name='countries', blank=True, to='shopping.Region', null=True),
        ),
    ]
