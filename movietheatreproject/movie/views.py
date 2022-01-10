from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie
from .serializers import NowShowingSerializer, ComingSoonSerializer  # ,MovieSeralizer


@api_view(['GET'])
def get_now_showing(request):
    now_showing = Movie.objects.raw('''
        SELECT id
        FROM movie_movie
        WHERE id IN (
            SELECT movie_id
            FROM showtime_showtime
        )
    ''')
    now_showing_serializer = NowShowingSerializer(now_showing, many=True)

    return Response(now_showing_serializer.data)


@api_view(['GET'])
def get_coming_soon(request):
    movies = Movie.objects.filter(coming_soon=True)
    coming_soon_serializer = ComingSoonSerializer(movies, many=True)

    return Response(coming_soon_serializer.data)
