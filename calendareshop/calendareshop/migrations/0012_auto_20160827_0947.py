# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0011_auto_20160823_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('name_cs', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=b'history/')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('description_cs', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('project_type', models.ForeignKey(related_name='histories', to='calendareshop.ProjectType')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='history_image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='history_text',
        ),
        migrations.RemoveField(
            model_name='project',
            name='history_text_cs',
        ),
        migrations.RemoveField(
            model_name='project',
            name='history_text_en',
        ),
    ]
