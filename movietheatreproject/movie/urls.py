from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('get-now-showing/', views.get_now_showing, name='get-now-showing'),
    path('get-coming-soon/', views.get_coming_soon, name='get-coming-soon'),
]
