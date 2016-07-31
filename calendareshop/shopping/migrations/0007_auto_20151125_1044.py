# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_auto_20151125_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='customorder',
            name='payment_type',
            field=models.CharField(default='cod', max_length=20, choices=[('cod', 'Platba p\u0159i p\u0159evzet\xed'), ('bank', 'Platba p\u0159evodem na \xfa\u010det')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customorder',
            name='shipping_type',
            field=models.CharField(max_length=20, choices=[(b'post', b'Post service'), (b'personal_prague', 'Personally in Prague \u0158epy (after clearing)'), (b'personal_frenstat', 'Personally in Fren\u0161t\xe1t p.R. (after clearing)')]),
        ),
    ]
