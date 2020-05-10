# flake8: noqa: E405
from rest_framework import generics, mixins, filters
from .serializers import *
from .permissions import *
from .pagination import *
from .filters import *
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from .algorithms import euclidean_distance, get_neighbors, NEIGHBOR_NUMBER, RATING_NUMBER, RECOMMEND_NUMBER


class UserPreferencesView(generics.RetrieveAPIView,
                          mixins.UpdateModelMixin):
    serializer_class = UserGenrePreferencesSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self):
        obj = get_object_or_404(UserProfile, user=self.request.user.id)
        return obj

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class WatchedListView(generics.RetrieveAPIView,
                      mixins.UpdateModelMixin):
    serializer_class = WatchedListSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self):
        obj = get_object_or_404(UserProfile, user=self.request.user.id)
        return obj

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class GenreCreateView(generics.CreateAPIView):
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUser,)


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return Genre.objects.all()


class GenreListView(generics.ListAPIView):
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Genre.objects.all()


class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return Movie.objects.all()


class MovieRetrieveView(generics.RetrieveAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Movie.objects.all()


class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
    ]

    search_fields = ['title']
    ordering_fields = ['title']

    def get_queryset(self):
        queryset = Movie.objects.all()
        genres_params = self.request.query_params.get('genre', [])

        # If genres filtering needed
        if genres_params:
            target_genres = eval(genres_params)

            for target_genre in target_genres:
                queryset = queryset.filter(genre__in=[target_genre])
        return queryset


class MovieRecommendView(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Convert Ratings into 2 dictionaries:
        #     my_ratings_dict - dictionary with ratings of current user (key = film, value = rating)
        #     other_ratings_dict - dictionary with other users' dictionaries (key = user, value = dicionary)
        #         every dictionary in other_ratings_dict is (key = film, value = rating)
        my_ratings = Rating.objects.filter(user=self.request.user)
        other_ratings = Rating.objects.exclude(user=self.request.user)[:RATING_NUMBER]
        my_ratings_dict = {}
        other_ratings_dict = {}
        for r in my_ratings:
            my_ratings_dict[r.film] = r.value
        for r in other_ratings:
            if r.user in other_ratings_dict:
                other_ratings_dict[r.user][r.film] = r.value
            else:
                other_ratings_dict[r.user] = {}

        # Get user ids of current user's nearest neighbors
        neighbors = get_neighbors(other_ratings_dict, my_ratings_dict)

        # Get top rated film ids from nearest neighbors
        recommendations, i = [], 0
        while len(recommendations) < RECOMMEND_NUMBER:
            user_i_ratings = other_ratings_dict[neighbors[i]]
            max_rated_film = max(user_i_ratings, key=user_i_ratings.get)
            recommendations.append(max_rated_film)
            del (other_ratings_dict[neighbors[i]][max_rated_film])
            i += 1
            if i >= NEIGHBOR_NUMBER:
                i = 0

        # Return Movie objects with ids from recommendations
        return recommendations


class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)


class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)


class RatingListView(generics.ListAPIView):
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Rating.objects.all()
