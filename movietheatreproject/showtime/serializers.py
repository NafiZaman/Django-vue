from rest_framework import serializers
from .models import Showtime


# class ShowtimeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Showtime
#         fields = ('id', 'theatre', 'show_times')
#         extra_kwargs = {
#             'id': {'read_only': True},
#         }


class NowShowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showtime
        fields = ('id', 'movie',)
        extra_kwargs = {
            'id': {'read_only': True},
        }
