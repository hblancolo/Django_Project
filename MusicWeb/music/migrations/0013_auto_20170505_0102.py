# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_song_song_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_file',
            field=models.FileField(upload_to=''),
        ),
    ]
