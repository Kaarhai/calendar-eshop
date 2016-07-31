# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0004_auto_20150918_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttype',
            name='codename',
            field=models.CharField(default='calendar', max_length=50, verbose_name='project code'),
            preserve_default=False,
        ),
    ]
