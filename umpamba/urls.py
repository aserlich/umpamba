from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'umpamba.views.home', name='home'),
    url(r'^newscoder/', include('newscoder.urls')),

    url(r'^admin/', include(admin.site.urls)),

    )
