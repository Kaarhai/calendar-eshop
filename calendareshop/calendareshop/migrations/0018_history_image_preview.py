# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0017_staticpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='image_preview',
            field=models.ImageField(default='', upload_to=b'history/'),
            preserve_default=False,
        ),
        migrations.RunSQL("UPDATE calendareshop_history SET image_preview=image;", migrations.RunSQL.noop)
    ]
