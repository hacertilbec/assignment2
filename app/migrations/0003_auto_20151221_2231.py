# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-21 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151221_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='times',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]
