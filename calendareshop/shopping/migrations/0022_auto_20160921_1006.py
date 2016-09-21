# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0020_project_motto'),
        ('shopping', '0021_product_translation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='project',
        ),
        migrations.AddField(
            model_name='product',
            name='projects',
            field=models.ManyToManyField(related_name='products', to='calendareshop.Project'),
        ),
    ]
