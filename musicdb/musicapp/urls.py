from models import Artist, Album, Track, Lyrics
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import DetailView, ListView, DeleteView
from views import ArtistDetail, AlbumDetail, TrackDetail, CreateArtist, CreateAlbum, DeleteElement
from views import CreateTrack, CreateLyrics, AlbumList, TrackList, LyricList, LoginRequiredCheckOwnerUpdateView
from forms import *

urlpatterns = [
    # List 30 first artists: /music/
    url(r'^$',ListView.as_view(
        queryset=Artist.objects.all().order_by('name')[:30],
        context_object_name='artists_list',
        template_name='musicapp/artist_list.html'),
        name='artist_list'
        ),
    url(r'^artists/$',ListView.as_view(
        queryset=Artist.objects.all().order_by('name')[:30],
        context_object_name='artists_list',
        template_name='musicapp/artist_list.html'),
        name='artist_list'
        ),
    
    # Show artist details: /music/artists/#/
    url(r'^artists/(?P<pk>\d+)/$',
     ArtistDetail.as_view(),
     name='artist_detail'),
    
    # Show artist album list: /music/artists/#/albums/
    url(r'^artists/(?P<pk>\d+)/albums/$',
     AlbumList.as_view(),
     name='album_list'),
    
    # Show artist album details: /music/artists/#/albums/#/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pk>\d+)/$',
     AlbumDetail.as_view(),
     name='album_detail'),
    
    # Show album track list: /music/artists/#/albums/#/tracks/#/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/$',
     TrackList.as_view(),
     name='track_list'),
    
    # Show track details: /music/artists/#/albums/#/tracks/#/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/(?P<pk>\d+)/$',
     TrackDetail.as_view(),
     name='track_detail'),
  
    # Show track lyrics list: /music/artists/#/albums/#/tracks/#/lyrics/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/(?P<pkt>\d+)/lyrics/$',
     LyricList.as_view(),
     name='lyrics_list'),
    
     
    # Show track lyrics: /music/artists/#/albums/#/tracks/#/lyrics/#/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/(?P<pkt>\d+)/lyrics/(?P<pk>\d+)/$',
     DetailView.as_view(model=Lyrics, template_name='musicapp/track_lyrics.html'),
     name='track_lyrics'),
    
    # Add a new artist: /music/artists/create/
    url(r'^artists/create/$',CreateArtist.as_view(),name='artist_create'),
    
    # Edit artist details: /music/artists/#/edit/
    url(r'^artists/(?P<pk>\d+)/edit/$',LoginRequiredCheckOwnerUpdateView.as_view(model=Artist, 
     template_name='musicapp/form.html',form_class=ArtistForm),name='artist_edit'),
     
    # Create a new album: /music/artists/#/albums/create/
    url(r'^artists/(?P<pk>\d+)/albums/create/$',CreateAlbum.as_view(),
    name='album_create'),
    
    # Edit album details: /music/artists/#/albums/#/edit/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pk>\d+)/edit/$',LoginRequiredCheckOwnerUpdateView.as_view(
        model=Album, template_name='musicapp/form.html',form_class=AlbumForm),name='album_edit'),
        
    # Create a new track: /music/artists/#/albums/#/tracks/create/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/create/$',
    CreateTrack.as_view(),name='track_create'),
    
    # Edit track details: /music/artists/#/albums/#/tracks/#/edit/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/(?P<pk>\d+)/edit/$',
    LoginRequiredCheckOwnerUpdateView.as_view(model=Track,form_class=TrackForm),
    name='track_edit'),

    # Create new lyrics: /music/artists/#/albums/#/tracks/#/lyrics/create/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/(?P<pk>\d+)/lyrics/create/$',
    CreateLyrics.as_view(),name='lyrics_create'),

    # Edit lyrics details: /music/artists/#/albums/#/tracks/#/lyrics/#/edit/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/(?P<pkc>\d+)/lyrics/(?P<pk>\d+)/edit/$',
    LoginRequiredCheckOwnerUpdateView.as_view(model=Lyrics,form_class=LyricForm)),

    #Delete artist
    url(r'^artists/(?P<pk>\d+)/delete/$',DeleteElement.as_view(model=Artist,
    template_name='musicapp/confirm_delete.html'),name='artist_delete'),

     # Delete album :
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pk>\d+)/delete/$',DeleteElement.as_view(
        model=Album, template_name='musicapp/confirm_delete.html'),name='album_delete'),

    # Delete track :
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/(?P<pk>\d+)/delete/$',
    DeleteElement.as_view(model=Track,template_name='musicapp/confirm_delete.html'),
    name='track_delete'),

    # Delete lyrics details:
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/(?P<pkc>\d+)/lyrics/(?P<pk>\d+)/delete/$',
    DeleteElement.as_view(model=Lyrics, template_name= 'musicapp/confirm_delete.html')),



]