from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('get-news/', views.get_news, name='get-news'),
]
