# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0010_newslettersubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='history_image',
            field=models.ImageField(upload_to=b'project_history/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='history_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='history_text_cs',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='history_text_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='text_header',
            field=models.CharField(default='About Draci.info calendar', max_length=b'255'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='text_header_cs',
            field=models.CharField(max_length=b'255', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='text_header_en',
            field=models.CharField(max_length=b'255', null=True),
        ),
    ]
