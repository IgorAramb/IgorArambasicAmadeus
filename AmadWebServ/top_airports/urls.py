from django.conf.urls import patterns, url

from top_airports import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)