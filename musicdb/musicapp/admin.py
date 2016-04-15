from django.contrib import admin
import models
# Register your models here.
admin.site.register(models.Album)
admin.site.register(models.Artist)
admin.site.register(models.Track)
admin.site.register(models.Search)
admin.site.register(models.SearchResultsAlbum)
admin.site.register(models.SearchResultsArtist)
admin.site.register(models.SearchResultsTrack)