# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]