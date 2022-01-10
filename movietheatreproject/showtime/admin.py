from django.contrib import admin
from showtime.models import Showtime


class ShowtimeAdmin(admin.ModelAdmin):
    search_fields = ['movie', ]
    ordering = ("-movie",)
    list_display = ("movie", "theatre", "show_times")

    # fieldsets = (
    #     ('Post Information', {'fields': ('op', 'text', 'date_added',)}),
    # )


admin.site.register(Showtime, ShowtimeAdmin)
