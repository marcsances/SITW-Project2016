from models import Artist, Album, Track, Lyrics
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import DetailView, ListView, UpdateView
from views import ArtistDetail, AlbumDetail, TrackDetail, CreateArtist, CreateAlbum, CreateTrack, CreateLyrics

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
    
    # Show artist album details: /music/artists/#/albums/#/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pk>\d+)/$',
     AlbumDetail.as_view(),
     name='album_detail'),
    
    # Show track details: /music/artists/#/albums/#/tracks/#/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/(?P<pk>\d+)/$',
     TrackDetail.as_view(),
     name='track_detail'),
     
    # Show track lyrics: /music/artists/#/albums/#/tracks/#/lyrics/#/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/(?P<pkt>\d+)/lyrics/(?P<pk>\d+)/$',
     DetailView.as_view(model=Lyrics, template_name='musicapp/track_lyrics.html'),
     name='track_lyrics'),
    
    # Add a new artist: /music/artists/create/
    url(r'^artists/create/$',CreateArtist.as_view(),name='artist_create'),
    
    # Edit artist details: /music/artists/#/edit/
    url(r'^artists/(?P<pk>\d+)/edit/$',UpdateView.as_view(model=Artist, 
     template_name='musicapp/form.html',form_class='artist_edit'),name='artist_edit'),
     
    # Create a new album: /music/artists/#/albums/create/
    url(r'^artists/(?P<pk>\d+)/albums/create/$',CreateAlbum.as_view(),
    name='album_create'),
    
    # Edit album details: /music/artists/#/albums/#/edit/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pk>\d+)$',UpdateView.as_view(
        model=Album, template_name='musicapp/form.html',form_class='album_edit')),
        
    # Create a new track: /music/artists/#/albums/#/tracks/create/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pk>\d+)/tracks/create/$',
    CreateTrack.as_view(),name='track_create'),
    
    # Edit track details: /music/artists/#/albums/#/tracks/#/edit/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/(?P<pk>\d+)/edit/$',
    UpdateView.as_view(model=Track,template_name='musicapp/form.html',form_class='track_edit')),

    # Create new lyrics: /music/artists/#/albums/#/tracks/#/lyrics/create/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pk>\d+)/tracks/(?P<pk>\d+)/lyrics/create/$',
    CreateLyrics.as_view(),name='lyrics_create'),

    # Edit lyrics details: /music/artists/#/albums/#/tracks/#/lyrics/#/edit/
    url(r'^artists/(?P<pka>\d+)/albums/(?P<pkb>\d+)/tracks/(?P<pkc>\d+)/lyrics/(?P<pk>\d+)/edit/$',
    UpdateView.as_view(model=Lyrics,template_name='musicapp/form.html',form_class='lyrics_edit')),
    
]