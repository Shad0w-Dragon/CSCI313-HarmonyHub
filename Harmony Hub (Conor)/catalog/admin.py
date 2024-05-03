from django.contrib import admin
from .models import Artist, Genre, Song, Album

# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Administration object for Genre models."""
    list_display = ('name',)
    # Add any other configurations as needed


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """Administration object for Artist models."""
    list_display = ('name', 'common_genre', 'top_song')
    # Add any other configurations as needed


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """Administration object for Song models."""
    list_display = ('title', 'artist', 'release_date', 'display_genre', 'length')
    # Add any other configurations as needed


admin.site.register(Album)