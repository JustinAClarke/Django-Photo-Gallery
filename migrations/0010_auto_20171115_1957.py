# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 08:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_nav'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Nav',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
