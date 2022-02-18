from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', obtain_auth_token, name='login'),
    path('logout', views.log_out, name='logout'),
    path('get-user-profile', views.get_user_profile, name='get-user-profile'),
    # path('', views.home_page),
    # path('register/<str:user_type>/', views.register, name='register'),
    # path('logout/', views.user_logout, name='user_logout'),
]