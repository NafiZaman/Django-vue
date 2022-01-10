import string
import random
from django.core.exceptions import ValidationError

from django.db import models
from django.utils.text import slugify
from django.apps import apps


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


def get_default_movie_details():
    return {
        'title': '',
        'synopsis': '',
        'release_date': '',
        'director': '',
    }


class Movie(models.Model):
    title = models.CharField(max_length=500)
    poster = models.URLField(max_length=500, blank=True, null=True)
    synopsis = models.TextField(max_length=2000, blank=True, null=True)
    details = models.JSONField(default=get_default_movie_details)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    coming_soon = models.BooleanField(default=False)

    def clean(self):
        if self.coming_soon:
            model_showtime = apps.get_model('showtime.Showtime')
            if model_showtime.objects.filter(movie=self.id).exists():
                raise ValidationError(
                    "Cannot set 'Coming Soon' property as object exists in Showtime table")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
