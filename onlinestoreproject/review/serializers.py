from rest_framework import serializers
from .models import *

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('key', 'user', 'title', 'product', 'text', 'rating', 'date_posted')