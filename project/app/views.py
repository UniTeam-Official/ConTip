from rest_framework import generics, mixins, filters
from .serializers import *
from .permissions import *
from .pagination import *
from .filters import *
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import django_filters
from django_filters.rest_framework import DjangoFilterBackend


class UserPreferencesView(generics.RetrieveAPIView,
                             mixins.UpdateModelMixin):
    serializer_class = UserGenrePreferencesSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_object(self):
        obj = get_object_or_404(UserProfile, user=self.request.user.id)
        return obj

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class WatchedListView(generics.RetrieveAPIView,
                             mixins.UpdateModelMixin):
    serializer_class = WatchedListSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_object(self):
        obj = get_object_or_404(UserProfile, user=self.request.user.id)
        return obj

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class GenreCreateView(generics.CreateAPIView):
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUser, )


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return Genre.objects.all()


class GenreListView(generics.ListAPIView):
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Genre.objects.all()


class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, )


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return Movie.objects.all()


class MovieRetrieveView(generics.RetrieveAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Movie.objects.all()


class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, )
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


class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated, )


class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)


class RatingListView(generics.ListAPIView):
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Rating.objects.all()
