# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0007_traveler_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveler',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]