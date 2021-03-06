# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-04 16:37
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicapp', '0004_auto_20160604_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=3, verbose_name='Rating')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='track',
            name='numReviews',
        ),
        migrations.RemoveField(
            model_name='track',
            name='reviews',
        ),
        migrations.AddField(
            model_name='trackreview',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.Track'),
        ),
        migrations.AddField(
            model_name='trackreview',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
