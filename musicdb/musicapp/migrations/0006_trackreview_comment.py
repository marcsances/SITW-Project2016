# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-08 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_auto_20160604_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackreview',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]