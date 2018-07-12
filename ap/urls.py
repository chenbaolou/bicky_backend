from django.conf.urls import url
from ap import views

urlpatterns = [
    url(r'^aptype/$', views.APTypeList.as_view()),
    url(r'^ap/$', views.APList.as_view()),
    url(r'^ap/(?P<pk>[0-9]+)/$', views.APDetail.as_view())
]