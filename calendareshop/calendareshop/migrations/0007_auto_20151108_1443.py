# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0006_auto_20151028_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('image', models.ImageField(upload_to=b'authors/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('link_da', models.URLField(verbose_name='DeviantArt', blank=True)),
                ('link_web', models.URLField(verbose_name='Personal website', blank=True)),
                ('link_fb', models.URLField(verbose_name='Facebook', blank=True)),
                ('link_email', models.URLField(verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='role',
            field=models.ForeignKey(related_name='authors', to='calendareshop.AuthorRole'),
        ),
        migrations.AddField(
            model_name='project',
            name='authors',
            field=models.ManyToManyField(related_name='projects', to='calendareshop.Author'),
        ),
    ]
