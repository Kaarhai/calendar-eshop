# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '__first__'),
        ('shopping', '0003_auto_20150923_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomOrder',
            fields=[
                ('order_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='shop.Order')),
                ('shipping_type', models.CharField(default=b'post', max_length=20, choices=[(b'post', 'Post service'), (b'personal_prague', 'Personally in Prague \u0158epy (after clearing)'), (b'personal_frenstat', 'Personally in Fren\u0161t\xe1t p.R. (after clearing)')])),
            ],
            options={
                'abstract': False,
            },
            bases=('shop.order',),
        ),
    ]
