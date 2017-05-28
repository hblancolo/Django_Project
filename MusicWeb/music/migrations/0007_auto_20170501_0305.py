# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 01:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20170501_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='song',
        ),
        migrations.AddField(
            model_name='artist',
            name='main_genre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Artist'),
        ),
    ]
