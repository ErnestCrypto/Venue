from django.contrib import admin
from .models import Venue, Artist, Shows


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'date', 'time']


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['venue', 'title', 'gender', 'contact']


@admin.register(Shows)
class ShowsAdmin(admin.ModelAdmin):
    list_display = ['artist', 'name', 'description']
