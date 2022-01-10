from django.contrib import admin
from .models import Theatre


class TheatreConfig(admin.ModelAdmin):
    search_fields = ['name', ]
    ordering = ("-name",)
    list_display = ("name", "location",)


admin.site.register(Theatre, TheatreConfig)
