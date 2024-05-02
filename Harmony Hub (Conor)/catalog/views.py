from django.shortcuts import render
from .models import Artist, Song, Genre

def index(request):
    """View function for home page of site."""
    num_songs = Song.objects.all().count()
    num_artists = Artist.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    return render(
        request,
        'index.html',
        context={'num_songs': num_songs, 'num_artists': num_artists,
                 'num_genres': num_genres, 'num_visits': num_visits},
    )

from django.views import generic

class SongListView(generic.ListView):
    """Generic class-based view for a list of songs."""
    model = Song
    paginate_by = 10

class SongDetailView(generic.DetailView):
    """Generic class-based detail view for a song."""
    model = Song

class ArtistListView(generic.ListView):
    """Generic class-based list view for a list of artists."""
    model = Artist
    paginate_by = 10

class ArtistDetailView(generic.DetailView):
    """Generic class-based detail view for an artist."""
    model = Artist

class GenreListView(generic.ListView):
    """Generic class-based list view for a list of genres."""
    model = Genre
    paginate_by = 10

class GenreDetailView(generic.DetailView):
    """Generic class-based detail view for a genre."""
    model = Genre

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class SongCreate(CreateView):
    model = Song
    fields = ['title', 'artist', 'release_date', 'genre', 'length']

class SongUpdate(UpdateView):
    model = Song
    fields = ['title', 'artist', 'release_date', 'genre', 'length']

class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('songs')

class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'common_genre', 'top_song']

class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'common_genre', 'top_song']

class ArtistDelete(DeleteView):
    model = Artist
    success_url = reverse_lazy('artists')

class GenreCreate(CreateView):
    model = Genre
    fields = ['name']

class GenreUpdate(UpdateView):
    model = Genre
    fields = ['name']

class GenreDelete(DeleteView):
    model = Genre
    success_url = reverse_lazy('genres')
