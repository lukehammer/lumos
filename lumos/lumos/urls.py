from django.conf.urls import patterns, url, include
from lumos import views

 #Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name= 'index'),
    url(r'^monkeys$', views.monkeys, name= 'monkeys'),
    url(r'^shows$',views.show,name='showform')

    # Examples:
    # url(r'^$', 'lumos.views.home', name='home'),
    # url(r'^lumos/', include('lumos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    )

#nothing changed 