# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-13 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0040_topperlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='testattendance',
            name='grade',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
    ]