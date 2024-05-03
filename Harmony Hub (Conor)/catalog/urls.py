from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.SongListView.as_view(), name='songs'),
    path('song/<int:pk>/', views.SongDetailView.as_view(), name='song-detail'),
    path('artists/', views.ArtistListView.as_view(), name='artists'),
    path('artist/<int:pk>/', views.ArtistDetailView.as_view(), name='artist-detail'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('genre/<int:pk>/', views.GenreDetailView.as_view(), name='genre-detail'),
    path('song/create/', views.SongCreate.as_view(), name='song-create'),
    path('song/<int:pk>/update/', views.SongUpdate.as_view(), name='song-update'),
    path('song/<int:pk>/delete/', views.SongDelete.as_view(), name='song-delete'),
    path('artist/create/', views.ArtistCreate.as_view(), name='artist-create'),
    path('artist/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist-update'),
    path('artist/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist-delete'),
    path('genre/create/', views.GenreCreate.as_view(), name='genre-create'),
    path('genre/<int:pk>/update/', views.GenreUpdate.as_view(), name='genre-update'),
    path('genre/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre-delete'),
    path('add_to_favorites/<int:song_id>/', views.add_to_favorites, name='add-to-favorites'),
    path('remove_from_favorites/<int:song_id>/', views.remove_from_favorites, name='remove-from-favorites'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/create/', views.create_account, name='create_account'), 
]
