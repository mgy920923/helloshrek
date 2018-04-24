# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-31 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('Year', models.CharField(max_length=5)),
                ('Plot', models.CharField(max_length=1500)),
                ('Genre', models.CharField(max_length=250)),
                ('Imdb_rating', models.FloatField(default=0.0)),
                ('Plot_outline', models.CharField(default=None, max_length=1000)),
                ('Director', models.CharField(default=None, max_length=50)),
                ('Poster', models.FileField(upload_to='')),
                ('Path', models.CharField(max_length=100)),
                ('Watched', models.BooleanField(default=False)),
                ('trailer', models.CharField(blank=True, default=None, max_length=150, null=True)),
            ],
        ),
    ]
