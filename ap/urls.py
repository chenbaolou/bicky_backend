"""
路由配置
"""
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('aptype/', views.APTypeList.as_view()),
    path('ap/', views.APList.as_view()),
    re_path(r'^ap/(?P<pk>[0-9]+)/$', views.APDetail.as_view()),
    path('ap/checkUnique/', views.check_ap_unique),
    path('ap/batch/', views.batch),
]