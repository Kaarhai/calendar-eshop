# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0005_projecttype_codename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttype',
            name='codename',
            field=models.CharField(unique=True, max_length=50, verbose_name='project code'),
        ),
    ]
