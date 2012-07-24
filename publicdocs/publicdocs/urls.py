from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'documents.views.index', name='index'),
    url(r'^category/(?P<slug>[-\w]+)/$', 'documents.views.category'),
    url(r'^author/(?P<slug>[-\w]+)/$', 'documents.views.author'),
    url(r'^document/(?P<slug>[-\w]+)/$', 'documents.views.document'),
    url(r'^search/', 'documents.views.search'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
