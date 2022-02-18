from django.urls import path
from . import views

urlpatterns = [
    path('get-reviews/<str:prod_key>', views.get_reviews, name='get-reviews'),
]