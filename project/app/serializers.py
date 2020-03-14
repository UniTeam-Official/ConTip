from rest_framework import serializers
from .models import *


class WatchedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("watched_list", )


class UserGenrePreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("genre_preferences", )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rating
        fields = "__all__"
