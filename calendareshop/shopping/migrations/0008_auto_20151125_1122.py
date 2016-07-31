# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0007_auto_20151125_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customorder',
            old_name='payment_type',
            new_name='payment_method',
        ),
    ]
