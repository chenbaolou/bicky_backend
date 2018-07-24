from django.urls import path
from . import views

urlpatterns = [
    path('user/login/', views.loginauth),
    path('user/current/', views.currentUser),
    path('user/logout/', views.logout),
]