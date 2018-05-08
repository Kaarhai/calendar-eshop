# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0028_GDPR fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customorder',
            name='personal_information_consent_years',
            field=models.PositiveIntegerField(default=20),
        ),
    ]
