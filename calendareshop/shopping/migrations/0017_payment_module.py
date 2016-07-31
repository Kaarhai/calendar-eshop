# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0016_auto_20160722_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='module',
            field=models.CharField(default='bank', max_length=10, verbose_name='module code', choices=[('paypal', 'PayPal'), ('cod', 'Cash on delivery'), ('bank', 'Bank transfer'), ('cash', 'Cash')]),
            preserve_default=False,
        ),
    ]
