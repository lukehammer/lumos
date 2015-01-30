from django.conf.urls import patterns, url
from lumosmagic import views

urlpatterns = patterns('',
    url(r'^index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'tricks/?', views.trick, name='trick'),
    url(r'dom/?', views.dom, name='dom'),
    url(r'^ajax/$', views.ajax, name='ajax')

    )

