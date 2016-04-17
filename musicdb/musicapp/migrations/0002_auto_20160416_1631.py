# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 16:31
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchresultsalbum',
            name='album_id',
        ),
        migrations.RemoveField(
            model_name='searchresultsalbum',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='searchresultsartist',
            name='artist_id',
        ),
        migrations.RemoveField(
            model_name='searchresultsartist',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='searchresultstrack',
            name='search_id',
        ),
        migrations.RemoveField(
            model_name='searchresultstrack',
            name='track_id',
        ),
        migrations.AddField(
            model_name='album',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artist',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lyrics',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='lyrics',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='track',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='track',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Search',
        ),
        migrations.DeleteModel(
            name='SearchResultsAlbum',
        ),
        migrations.DeleteModel(
            name='SearchResultsArtist',
        ),
        migrations.DeleteModel(
            name='SearchResultsTrack',
        ),
    ]