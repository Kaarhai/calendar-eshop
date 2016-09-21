# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0022_auto_20160921_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='code',
            field=models.CharField(default='', max_length=10, verbose_name='code'),
            preserve_default=False,
        ),
    ]
