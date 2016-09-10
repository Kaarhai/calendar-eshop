# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0015_auto_20160827_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='description_cs',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='description_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RunSQL("UPDATE calendareshop_projectimage SET description_cs=description, description_en=description;", migrations.RunSQL.noop)
    ]
