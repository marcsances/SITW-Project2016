from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from forms import *
from models import Track, Artist, Album, Lyrics
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin,self).dispatch(*args,**kwargs)

class CheckOwnerMixin(object):
    def get_object(self,*args,**kwargs):
        obj = super(CheckOwnerMixin,self).get_object(*args, **kwargs)
        if (not obj.user==self.request.user):
            raise PermissionDenied
        return obj
        
class LoginRequiredCheckOwnerUpdateView(LoginRequiredMixin,CheckOwnerMixin,UpdateView):
    template_name = 'musicapp/form.html'

class AlbumList(ListView):
    template_name='musicapp/album_list.html'
    context_object_name='album_list'
    
    def get_queryset(self):
        self.artist_id = get_object_or_404(Artist, pk = self.kwargs['pk'])
        return Album.objects.filter(artist_id=self.artist_id)
        
class TrackList(ListView):
    template_name='musicapp/track_list.html'
    context_object_name='track_list'
    
    def get_queryset(self):
        self.album_id = get_object_or_404(Album, pk = self.kwargs['pka'])
        return Track.objects.filter(album_id=self.album_id)
        
class LyricList(ListView):
    template_name='musicapp/lyric_list.html'
    context_object_name='lyric_list'
    
    def get_queryset(self):
        self.track_id = get_object_or_404(Track, pk = self.kwargs['pkt'])
        return Lyrics.objects.filter(track_id=self.track_id)

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
    
class CreateArtist(LoginRequiredMixin,CreateView):
    model=Artist
    template_name='musicapp/form.html'
    form_class=ArtistForm
    
class CreateAlbum(LoginRequiredMixin,CreateView):
    model=Album
    template_name='musicapp/form.html'
    form_class=AlbumForm
    
class CreateTrack(LoginRequiredMixin,CreateView):
    model=Track
    template_name='musicapp/form.html'
    form_class=TrackForm

class CreateLyrics(LoginRequiredMixin,CreateView):
    model = Lyrics
    template_name='musicapp/form.html'
    form_class = LyricForm
