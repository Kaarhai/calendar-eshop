# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_voter_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 27, 17, 27, 29, 157569), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='votedimage',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 27, 17, 27, 41, 182383), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voter',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 27, 17, 27, 43, 573522), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vote',
            name='month',
            field=models.PositiveIntegerField(choices=[(0, b'\xc3\xbavod'), (1, b'leden'), (2, b'\xc3\xbanor'), (3, b'b\xc5\x99ezen'), (4, b'duben'), (5, b'kv\xc4\x9bten'), (6, b'\xc4\x8derven'), (7, b'\xc4\x8dervenec'), (8, b'srpen'), (9, b'z\xc3\xa1\xc5\x99\xc3\xad'), (10, b'\xc5\x99\xc3\xadjen'), (11, b'listopad'), (12, b'prosinec')]),
        ),
    ]
