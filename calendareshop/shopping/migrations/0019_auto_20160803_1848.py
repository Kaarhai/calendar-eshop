# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0018_auto_20160803_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='name_cs',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='payment',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='shipping',
            name='name_cs',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='shipping',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
    ]
