from django.core.exceptions import ValidationError
from django.db import models
from movie.models import Movie
from theatre.models import Theatre
from django.contrib.postgres.fields import ArrayField


class Showtime(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(
        Theatre, on_delete=models.CASCADE)

    show_times = ArrayField(models.TimeField(
        null=False, blank=False, default="{5:10 pm}"), blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['movie', 'theatre'], name='showtime'),
        ]

    def clean(self):
        if self.movie.coming_soon:
            raise ValidationError("This movie is listed as coming soon")

    def __str__(self):
        return str(self.movie)
