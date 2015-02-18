from django.conf.urls import patterns, url
from lumosmagic import views

urlpatterns = patterns('',
    url(r'^index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'tricks/?', views.trick, name='trick'),
    url(r'dom/?', views.dom, name='dom'),
    url(r'^ajax/$', views.ajax, name='ajax'),
<<<<<<< HEAD
    url(r'^show_builder/?$', views.show_builder, name='show_builder'),
    url(r'^navagation/?$', views.navagation, name='navagation'),
=======
    url(r'^show_builder/?$', views.show_builder, name='show_builder')
>>>>>>> 28be70440ac8e95134e156a58c485c17c13e226e

    )

