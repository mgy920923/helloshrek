# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-11 02:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20180410_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='Path',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='age',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='job',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='time_modified',
        ),
    ]
