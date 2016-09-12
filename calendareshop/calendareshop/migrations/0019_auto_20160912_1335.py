# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0018_history_image_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticpage',
            name='content_cs',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='staticpage',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.RunSQL("UPDATE calendareshop_staticpage SET content_cs=content, content_en=content;", migrations.RunSQL.noop)
    ]
