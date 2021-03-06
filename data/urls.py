from django.conf.urls import patterns, url
from data import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^happiness/$', views.happiness, name='happiness'),
    url(r'^sleep/$', views.sleep, name='sleep'),
    url(r'^summary/$', views.summary, name='summary'),
    url(r'^edit/(?P<date>[0-9]+)/$', views.edit, name='edit')
)