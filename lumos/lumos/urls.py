from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lumos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^lumosmagic/', include("lumosmagic.urls")),
    url(r'^$', include("lumosmagic.urls")),
    #url(r'^$',include(admin.site.urls))
)
