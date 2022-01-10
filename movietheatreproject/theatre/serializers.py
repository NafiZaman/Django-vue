from rest_framework import serializers
from .models import Theatre


class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = ('id', 'name', 'location')
        extra_kwargs = {
            'id': {'read_only': True},
        }
