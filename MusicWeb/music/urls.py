from django.conf.urls import include, url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/<song_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'^song/add/$', views.SongCreate.as_view(), name='song-add'),

    # /music/album/2/
    url(r'^song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name='song-update'),


    # Actually i'm not using the delete function because I don't have any "Delete" button in html to assign it
    # /music/album/2/delete
    url(r'^song/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),

    url(r'^search/', include('search.urls')),
]