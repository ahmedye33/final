# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 06:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addpost', '0003_blog_hobbyitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='publish',
        ),
    ]
