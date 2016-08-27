# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0014_auto_20160827_1012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectimage',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='projectimage',
            name='image_preview',
            field=models.ImageField(default='', upload_to=b'projects/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
        ),
    ]
