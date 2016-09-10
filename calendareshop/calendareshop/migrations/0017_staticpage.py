# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0016_project_image_translation'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('name_cs', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True, verbose_name='slug')),
                ('slug_cs', autoslug.fields.AutoSlugField(null=True, populate_from=b'name', editable=False, unique=True, verbose_name='slug')),
                ('slug_en', autoslug.fields.AutoSlugField(null=True, populate_from=b'name', editable=False, unique=True, verbose_name='slug')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
