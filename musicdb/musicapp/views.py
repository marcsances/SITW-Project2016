from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from forms import *
from models import Track, Artist, Album, Lyrics

class ArtistDetail(DetailView):
    model=Artist
    template_name='musicapp/artist_detail.html'
    
class AlbumDetail(DetailView):
    model=Album
    template_name='musicapp/album_detail.html'
    
class TrackDetail(DetailView):
    model=Track
    template_name='musicapp/track_detail.html'

class LyricsDetail(DetailView):
    model=Lyrics
    template_name = 'musicapp/track_lyrics.html'
    
class CreateArtist(CreateView):
    model=Artist
    template_name='musicapp/form.html'
    form_class=ArtistForm
    
class CreateAlbum(CreateView):
    model=Album
    template_name='musicapp/form.html'
    form_class=AlbumForm
    
class CreateTrack(CreateView):
    model=Track
    template_name='musicapp/form.html'
    form_class=TrackForm

class CreateLyrics(CreateView):
    model = Lyrics
    template_name='musicapp/form.html'
    form_class = LyricsForm
