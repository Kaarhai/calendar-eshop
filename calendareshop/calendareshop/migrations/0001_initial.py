# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('name_cs', models.CharField(max_length=255, null=True)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, editable=False)),
                ('slug_cs', autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, null=True, editable=False)),
                ('slug_en', autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, null=True, editable=False)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('text_cs', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'projects/')),
                ('project', models.ForeignKey(related_name='images', to='calendareshop.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('name_cs', models.CharField(max_length=255, null=True)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_plural', models.CharField(max_length=255)),
                ('name_plural_cs', models.CharField(max_length=255, null=True)),
                ('name_plural_en', models.CharField(max_length=255, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, editable=False)),
                ('slug_cs', autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, null=True, editable=False)),
                ('slug_en', autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, null=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(related_name='projects', to='calendareshop.ProjectType'),
        ),
    ]
