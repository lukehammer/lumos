from django.conf.urls import patterns, url
from lumos_app import views

urlpatterns = patterns('',
    url(r'^index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'tricks/?', views.trick, name='trick'),
    url(r'dom/?', views.dom, name='dom'),
    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^navagation/?$', views.navagation, name='navagation'),
    url(r'^show_builder/?$', views.show_builder, name='show_builder'),

    )

