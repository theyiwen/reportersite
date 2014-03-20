from django.conf.urls import patterns, url
from data import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^happiness/$', views.happiness, name='happiness'),
    url(r'^sleep/$', views.sleep, name='sleep')

)