# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0027_product_items_in_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='customorder',
            name='personal_information_consent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customorder',
            name='personal_information_consent_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customorder',
            name='personal_information_consent_years',
            field=models.PositiveIntegerField(default=70),
        ),
    ]
