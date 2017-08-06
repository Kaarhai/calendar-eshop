# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='season',
            field=models.CharField(max_length=6, choices=[(b'intro', b'\xc3\xbavod'), (b'spring', b'jaro'), (b'summer', b'l\xc3\xa9to'), (b'autumn', b'podzim'), (b'winter', b'zima')]),
        ),
        migrations.AlterField(
            model_name='votedimage',
            name='season',
            field=models.CharField(max_length=6, choices=[(b'intro', b'\xc3\xbavod'), (b'spring', b'jaro'), (b'summer', b'l\xc3\xa9to'), (b'autumn', b'podzim'), (b'winter', b'zima')]),
        ),
        migrations.AlterField(
            model_name='voter',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
