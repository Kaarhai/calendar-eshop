# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0012_auto_20160827_0947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ['date_created'], 'verbose_name_plural': 'histories'},
        ),
        migrations.AddField(
            model_name='history',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
        ),
    ]
