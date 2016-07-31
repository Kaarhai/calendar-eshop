# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='background_image',
            field=models.ImageField(upload_to=b'project_backgrounds/', blank=True),
        ),
    ]
