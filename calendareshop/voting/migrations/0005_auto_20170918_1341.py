# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0022_auto_20170827_2009'),
        ('voting', '0004_auto_20170827_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votedimage',
            name='author',
        ),
        migrations.AddField(
            model_name='votedimage',
            name='authors',
            field=models.ManyToManyField(related_name='images', to='calendareshop.Author'),
        ),
    ]
