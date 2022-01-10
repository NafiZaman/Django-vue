from rest_framework import serializers
from .models import Movie


class MovieSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster', 'synopsis', 'details',)
        extra_kwargs = {
            'id': {'read_only': True},
        }


class NowShowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster', 'slug')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class ComingSoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster')
        extra_kwargs = {
            'id': {'read_only': True},
        }
