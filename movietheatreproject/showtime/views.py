from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Showtime
from movie.models import Movie
from theatre.models import Theatre


@api_view(['GET'])
def get_showtime(request, movie_id):
    showtimes = Showtime.objects.filter(movie=movie_id)
    data = {'movie': {}, 'theatre_info': []}

    movie = Movie.objects.get(id=movie_id)
    data['movie']['title'] = movie.title
    data['movie']['poster'] = movie.poster
    data['movie']['synopsis'] = movie.synopsis
    data['movie']['details'] = movie.details

    for showtime in showtimes:
        theatre_info = Theatre.objects.filter(
            id=showtime.theatre.id).values('name', 'location').first()
        theatre_info['showtimes'] = showtime.show_times
        data['theatre_info'].append(theatre_info)

    return Response(data)
