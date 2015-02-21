from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lumos_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^lumos_app/', include("lumos_app.urls")),
    url(r'^$', include("lumos_app.urls")),
    #url(r'^$',include(admin.site.urls))
)
