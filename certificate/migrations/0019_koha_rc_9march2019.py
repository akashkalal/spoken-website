# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-04 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0018_auto_20190531_0506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koha_RC_9march2019',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('usertype', models.CharField(default='cc', max_length=10)),
                ('rcid', models.CharField(max_length=500)),
                ('remote', models.CharField(max_length=500)),
                ('purpose', models.CharField(default='KRC', max_length=10)),
            ],
        ),
    ]
