from django.urls import path
from . import views

app_name = 'showtime'

urlpatterns = [
    # path('get-now-showing/', views.get_now_showing, name='get-now-showing'),
    path('get-showtime/<str:movie_id>/',
         views.get_showtime, name='get-showtime'),
]
