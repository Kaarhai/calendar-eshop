# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0013_auto_20160827_1001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ['order'], 'verbose_name_plural': 'histories'},
        ),
        migrations.AddField(
            model_name='projectimage',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
