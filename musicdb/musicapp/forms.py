from django.forms import ModelForm
from models import Track, Artist, Album, Lyrics
class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ('user','date')

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ('user','date')
        
class TrackForm(ModelForm):
    class Meta:
        model = Track
        exclude = ('user','date')