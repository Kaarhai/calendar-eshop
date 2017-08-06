# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0020_project_motto'),
        ('voting', '0002_auto_20170806_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='author',
            field=models.OneToOneField(null=True, blank=True, to='calendareshop.Author'),
        ),
    ]
