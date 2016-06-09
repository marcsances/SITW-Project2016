from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView, RedirectView
from django.contrib.auth.models import User
from forms import *
from models import Track, Artist, Album, Lyrics, TrackReview
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy, reverse


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
        self.album_id = get_object_or_404(Album, pk = self.kwargs['pkb'])
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

    def get_context_data(self, **kwargs):
        context = super(TrackDetail,self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = TrackReview.RATING_CHOICES
        return context

class LyricsDetail(DetailView):
    model=Lyrics
    template_name = 'musicapp/track_lyrics.html'
    
class CreateArtist(LoginRequiredMixin,CreateView):
    model=Artist
    template_name='musicapp/form_artist.html'
    form_class=ArtistForm
    
    def form_valid(self, form):
        pop = form.save(commit=False)
        pop.user = User.objects.get(username=self.request.user)
        pop.save()
        return HttpResponseRedirect("../")
    
class CreateAlbum(LoginRequiredMixin,CreateView):
    model=Album
    template_name='musicapp/form_album.html'
    form_class=AlbumForm
    
    def form_valid(self, form):
        pop = form.save(commit=False)
        pop.user = User.objects.get(username=self.request.user)
        pop.save()
        return HttpResponseRedirect("../")
    
class CreateTrack(LoginRequiredMixin,CreateView):
    model=Track
    template_name='musicapp/form_track.html'
    form_class=TrackForm
    
    def form_valid(self, form):
        pop = form.save(commit=False)
        pop.user = User.objects.get(username=self.request.user)
        pop.save()
        return HttpResponseRedirect("../")

class CreateLyrics(LoginRequiredMixin,CreateView):
    model = Lyrics
    template_name='musicapp/form_lyrics.html'
    form_class = LyricForm
    
    def form_valid(self, form):
        pop = form.save(commit=False)
        pop.user = User.objects.get(username=self.request.user)
        pop.save()
        return HttpResponseRedirect("../")

class DeleteElement(LoginRequiredMixin,CheckOwnerMixin,DeleteView):
    template_name = 'musicapp/confirm_delete.html'
    def get_success_url(self):
        return '../../'

def review(request,pka,pkb,pkc):
    artist =  get_object_or_404(Artist, pk=pka)
    album =  get_object_or_404(Album, pk=pkb)
    track = get_object_or_404(Track, pk=pkc)
    review = TrackReview(rating= request.POST['rating'],
                         comment = request.POST['comment'],
                         user = request.user,
                         track=track)
    review.save()
    return HttpResponseRedirect(reverse('musicapp:track_detail', args=( artist.id,album.id, track.id,)))


class DeleteReview(LoginRequiredMixin,CheckOwnerMixin,DeleteView):
    template_name = 'musicapp/confirm_delete.html'
    def get_success_url(self):
        return '../../../'




