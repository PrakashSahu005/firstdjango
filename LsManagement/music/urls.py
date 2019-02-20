from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^add/$',views.addAlbum),
    url(r'^signup/$',views.signUp),
    url(r'^registerUsers/$',views.registerUsers),
    url(r'^signIn/$',views.signIn),
    url(r'^addMusicAlbum/$',views.addMusicAlbum),
    # url('emp', views.emp),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail),
    url(r'^learn/$', views.showForm),
    url(r'^countss/$', views.showCount, name='count'),
    url(r'^home/$', views.showForm, name='home')
]