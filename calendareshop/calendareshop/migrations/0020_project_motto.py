# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0019_auto_20160912_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='motto',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='motto_cs',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='motto_en',
            field=models.TextField(null=True, blank=True),
        ),
    ]
