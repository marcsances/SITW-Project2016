from django.shortcuts import render

from .models import Track

# Create your views here.
def tracks(request):
    tra = Track.objects.all()
    return render(request, '', {'tra': tra})


