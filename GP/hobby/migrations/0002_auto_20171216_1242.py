# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobbycat',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='hobbyitem',
            name='label_tag',
        ),
        migrations.AddField(
            model_name='hobbycat',
            name='hobbycat_disc',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
