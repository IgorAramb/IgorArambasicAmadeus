from django.conf.urls import patterns, url

from top_airports_json import views

urlpatterns = patterns('',
    url(r'^$', views.top_airports_json, name='top_airports_json')
)