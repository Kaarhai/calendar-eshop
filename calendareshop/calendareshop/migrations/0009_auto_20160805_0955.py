# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0008_auto_20151108_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='link_email',
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail', blank=True),
        ),
    ]
