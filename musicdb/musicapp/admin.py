from django.contrib import admin
import models
# Register your models here.
admin.site.register(models.Album)
admin.site.register(models.Artist)
admin.site.register(models.Track)
admin.site.register(models.Lyrics)
admin.site.register(models.TrackReview)