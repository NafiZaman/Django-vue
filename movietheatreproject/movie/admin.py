from django.contrib import admin
from movie.models import Movie


class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    ordering = ("title",)
    list_display = ("title", "coming_soon")


admin.site.register(Movie, MovieAdmin)
