# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-20 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0004_auto_20180820_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=50)),
                ('trackid', models.CharField(max_length=20)),
                ('isDetele', models.BooleanField(default=False)),
            ],
        ),
    ]
