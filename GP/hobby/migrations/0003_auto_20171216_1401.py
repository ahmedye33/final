# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0002_auto_20171216_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobbyitem',
            name='file_type',
        ),
        migrations.AddField(
            model_name='hobbyitem',
            name='hobbyitem_logo',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
