# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0007_auto_20151108_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorrole',
            name='name_cs',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='authorrole',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
    ]
