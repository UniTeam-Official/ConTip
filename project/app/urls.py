from django.urls import path, include
from .views import *

urlpatterns = [
    path(
        'preferences/set/',
        UserPreferencesView.as_view()
    ),
    path(
        'watched/set/',
        WatchedListView.as_view()
    ),
    path(
        'genre/create/',
        GenreCreateView.as_view()
    ),
    path(
        'genre/detail/<int:pk>',
        GenreDetailView.as_view()
    ),
    path(
        'genre/list/',
        GenreListView.as_view()
    ),
    # PREFERENCES VIEWS
    #FILM VIEWS
    path(
        'film/create/',
        MovieCreateView.as_view()
    ),
    path(
        'film/detail/<int:pk>',
        MovieDetailView.as_view()
    ),
    path(
        'film/list/',
        MovieListView.as_view()
    ),
    # RATINGS VIEWS
    path(
        'rating/create/',
        RatingCreateView.as_view()
    ),
    path(
        'rating/detail/<int:pk>/',
        RatingDetailView.as_view()
    ),
    path(
        'rating/list/',
        RatingCreateView.as_view()
    ),
]
