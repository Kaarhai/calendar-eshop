# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0008_auto_20151125_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customorder',
            name='payment_method',
            field=models.CharField(max_length=20, choices=[('cod', 'Cash on delivery'), ('bank', 'Bank transfer'), ('cash', 'Cash')]),
        ),
        migrations.AlterField(
            model_name='customorder',
            name='shipping_type',
            field=models.CharField(max_length=20, choices=[(b'post', 'Post service'), (b'personal_prague', 'Personally in Prague \u0158epy'), (b'personal_frenstat', 'Personally in Fren\u0161t\xe1t p.R.')]),
        ),
    ]
