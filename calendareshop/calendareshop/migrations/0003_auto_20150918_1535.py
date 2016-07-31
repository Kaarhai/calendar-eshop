# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0002_project_background_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 18, 15, 35, 40, 324283), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 18, 15, 35, 53, 548470), auto_now_add=True),
            preserve_default=False,
        ),
    ]
