# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-20 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0002_nav'),
    ]

    operations = [
        migrations.CreateModel(
            name='mustBuyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=50)),
                ('trackid', models.CharField(max_length=20)),
                ('isDetele', models.BooleanField(default=False)),
            ],
        ),
    ]
