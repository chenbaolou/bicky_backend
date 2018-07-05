from django.conf.urls import url
from mytest import views

urlpatterns = [
    url(r'^album/$', views.AlbumList.as_view()),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),
    url(r'^track/$', views.TrackList.as_view()),
    url(r'^track/(?P<pk>[0-9]+)/$', views.TrackDetail.as_view()),
]