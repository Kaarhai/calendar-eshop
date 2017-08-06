# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendareshop', '0020_project_motto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season', models.CharField(max_length=6, choices=[(b'spring', b'jaro'), (b'summer', b'l\xc3\xa9to'), (b'autumn', b'podzim'), (b'winter', b'zima')])),
                ('month', models.PositiveIntegerField(choices=[(1, b'leden'), (2, b'\xc3\xbanor'), (3, b'b\xc5\x99ezen'), (4, b'duben'), (5, b'kv\xc4\x9bten'), (6, b'\xc4\x8derven'), (7, b'\xc4\x8dervenec'), (8, b'srpen'), (9, b'z\xc3\xa1\xc5\x99\xc3\xad'), (10, b'\xc5\x99\xc3\xadjen'), (11, b'listopad'), (12, b'prosinec')])),
            ],
        ),
        migrations.CreateModel(
            name='VotedImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'voted_images/')),
                ('season', models.CharField(max_length=6, choices=[(b'spring', b'jaro'), (b'summer', b'l\xc3\xa9to'), (b'autumn', b'podzim'), (b'winter', b'zima')])),
                ('author', models.ForeignKey(related_name='images', to='calendareshop.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='vote',
            name='image',
            field=models.ForeignKey(related_name='votes', to='voting.VotedImage'),
        ),
        migrations.AddField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(related_name='votes', to='voting.Voter'),
        ),
    ]
