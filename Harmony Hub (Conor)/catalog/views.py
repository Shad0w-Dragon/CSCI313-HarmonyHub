from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Artist, Song, Genre, Favorite, CustomUser
from .forms import SignUpForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm


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


class SongListView(generic.ListView):
    """Generic class-based view for a list of songs."""
    model = Song
    paginate_by = 10


class SongDetailView(generic.DetailView):
    """Generic class-based detail view for a song."""
    model = Song

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_favorite'] = Favorite.objects.filter(user=self.request.user, song=self.object).exists()
        return context


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


@login_required
def add_to_favorites(request, song_id):
    """View function to add a song to favorites."""
    song = Song.objects.get(id=song_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, song=song)
    if created:
        return redirect('song-detail', pk=song_id)
    else:
        return redirect('index')  # Redirect to a suitable page if already favorited


@login_required
def remove_from_favorites(request, song_id):
    """View function to remove a song from favorites."""
    favorite = Favorite.objects.filter(user=request.user, song_id=song_id)
    if favorite.exists():
        favorite.delete()
    return redirect('index') 



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the home page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def create_account(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = SignUpForm()
    return render(request, 'registration/create_account.html', {'form': form})