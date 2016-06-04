from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import date
from django.core.urlresolvers import reverse

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
        
    def get_absolute_url(self):
        return reverse('musicapp:artist_detail',kwargs={'pk':self.pk})


class Album(models.Model):
    artist_id = models.ForeignKey(Artist)
    title = models.TextField(blank=False, null=False)
    duration = models.IntegerField()
    trackCount = models.IntegerField()
    releaseDate = models.DateTimeField(blank=True, null=True) # TBA albums might not have a date yet
    albumLink = models.TextField(blank=True, null=True)
    albumCoverurl = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    def __unicode__(self):
        return u"%s" % self.title
    def get_absolute_url(self):
        return reverse('musicapp:album_detail',kwargs={'pk':self.pk,'pka':self.artist_id.pk})	
        
class Track(models.Model):
    album_id = models.ForeignKey(Album)
    title = models.TextField(blank=False, null=False)
    duration = models.IntegerField()
    trackLink = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    def __unicode__(self):
        return u"%s" % self.title
    def get_absolute_url(self):
        return reverse('musicapp:track_detail',kwargs={'pk':self.pk,'pka':self.album_id.pk,
         'pkb':self.album_id.artist_id.pk})
        
class Lyrics(models.Model):
    track_id = models.ForeignKey(Track)
    lyrics = models.TextField()
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    def __unicode__(self):
        return u"%s" % self.lyrics
    def get_absolute_url(self):
        return reverse('musicapp:track_lyrics',kwargs={'pk':self.pk,'pka':self.track_id.album_id.pk,
         'pkb':self.track_id.album_id.artist_id.pk,'pkt':self.track_id.pk})

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2,'two'),(3,'three'),(4,'four'),(5,'five'))
    rating = models.PositiveSmallIntegerField('Rating', blank=False, default=3, choices=RATING_CHOICES)
    user= models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class TrackReview(Review):
    track = models.ForeignKey(Track)