from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView


class Genre(models.Model):
    """Model representing a music genre (e.g. Pop, Rock, Jazz)."""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a music genre (e.g. Pop, Rock, Jazz, Hip Hop, etc.)"
    )

    def __str__(self):
        """String representation of the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a particular genre instance."""
        return reverse('genre-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message="Genre already exists (case insensitive match)"
            ),
        ]


class Song(models.Model):
    """Model representing a song."""
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    release_date = models.DateField(null=True, blank=True)
    genre = models.ForeignKey(
        Genre, on_delete=models.RESTRICT, null=True, help_text="Select a genre for this song")
    length = models.DurationField(null=True, blank=True, help_text="Duration of the song")
    album = models.ForeignKey('Album', on_delete=models.CASCADE, help_text="Select the album this song belongs to", null=True)

    class Meta:
        ordering = ['title']

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        if self.genre:
            return self.genre.name
        else:
            return "No genre"

    display_genre.short_description = 'Genre'

    display_genre.short_description = 'Genre'

    def display_artist(self):
        """Creates a string for the Artist. This is required to display artist in Admin."""
        return self.artist.name if self.artist else 'Unknown'

    display_artist.short_description = 'Artist'

    def get_absolute_url(self):
        """Returns the URL to access a particular song."""
        return reverse('song-detail', args=[str(self.id)])

    def __str__(self):
        """String representation of the model object."""
        return self.title


class Artist(models.Model):
    """Model representing an artist."""
    name = models.CharField(max_length=255)
    common_genre = models.CharField(max_length=100)
    top_song = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the URL to access a particular artist instance."""
        return reverse('artist-detail', args=[str(self.id)])

    def __str__(self):
        """String representation of the model object."""
        return self.name


class Favorite(models.Model):
    """Model representing a user's favorite song."""
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'song')


class CustomUser(AbstractUser):
    """Custom user model."""
    favorite_genre = models.CharField(max_length=100)
    favorite_songs = models.ManyToManyField('Song', through='Favorite')

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        pass

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions'
    )


class Album(models.Model):
    """Model representing an album."""
    name = models.CharField(max_length=255)
    common_genre = models.CharField(max_length=100)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, help_text="Select album artist")

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the URL to access a particular album instance."""
        return reverse('album-detail', args=[str(self.id)])

    def __str__(self):
        """String representation of the model object."""
        return self.name
