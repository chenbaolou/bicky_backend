from django.urls import path
from . import views

urlpatterns = [
    path('system/sysinfo/', views.sysinfo),
]