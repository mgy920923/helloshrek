# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-12 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_movie_rating_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating_Count',
            field=models.IntegerField(default=0),
        ),
    ]
