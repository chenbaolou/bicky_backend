from django.urls import path
from . import views

urlpatterns = [
    path('user/login/', views.loginauth),
    path('user/current/', views.current_user),
    path('user/logout/', views.logout),
]