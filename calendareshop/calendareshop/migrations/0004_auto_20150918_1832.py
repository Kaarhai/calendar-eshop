# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0003_auto_20150918_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='projecttype',
            options={'ordering': ['-name']},
        ),
        migrations.AddField(
            model_name='projecttype',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 18, 18, 32, 32, 133222), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name_cs',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug_cs',
            field=autoslug.fields.AutoSlugField(null=True, populate_from=b'name', editable=False, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug_en',
            field=autoslug.fields.AutoSlugField(null=True, populate_from=b'name', editable=False, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='name_cs',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='name_plural',
            field=models.CharField(max_length=100, verbose_name='plural name'),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='name_plural_cs',
            field=models.CharField(max_length=100, null=True, verbose_name='plural name'),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='name_plural_en',
            field=models.CharField(max_length=100, null=True, verbose_name='plural name'),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='slug_cs',
            field=autoslug.fields.AutoSlugField(null=True, populate_from=b'name', editable=False, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='slug_en',
            field=autoslug.fields.AutoSlugField(null=True, populate_from=b'name', editable=False, unique=True, verbose_name='slug'),
        ),
    ]
