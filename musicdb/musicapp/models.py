from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from datetime import date

# Create your models here.

class Artist(models.Model):
    name = models.TextField(blank=False, null=False)
    artistLink = models.TextField(blank=True, null=True)
    artistPictureurl = models.TextField(blank=True, null=True)
    albumCount = models.IntegerField()
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    def __unicode__(self):
        return u"%s" % self.name

class Album(models.Model):
    artist_id = models.ForeignKey(Artist)
    title = models.TextField(blank=False, null=False)
    duration = models.DurationField()
    trackCount = models.IntegerField()
    releaseDate = models.DateTimeField(blank=True, null=True) # TBA albums might not have a date yet
    albumLink = models.TextField(blank=True, null=True)
    albumCoverurl = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    def __unicode__(self):
        return u"%s" % self.title
        
class Track(models.Model):
    album_id = models.ForeignKey(Album)
    title = models.TextField(blank=False, null=False)
    duration = models.DurationField()
    trackLink = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    def __unicode__(self):
        return u"%s" % self.title
        
class Lyrics(models.Model):
    track_id = models.ForeignKey(Track)
    lyrics = models.TextField()
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    def __unicode__(self):
        return u"%s" % self.lyrics
