# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_logo',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
