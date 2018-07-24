from django.urls import path
from . import views

urlpatterns = [
    path('notice/', views.load),
]