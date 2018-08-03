from django.urls import path
from . import views

urlpatterns = [
    path('common/upload/', views.upload),
]