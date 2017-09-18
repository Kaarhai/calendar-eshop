# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_auto_20170918_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='voting_finished',
            field=models.BooleanField(default=False),
        ),
    ]
