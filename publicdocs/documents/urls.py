from django.conf.urls import patterns, include, url


urlpatterns = patterns('documents.views',
    url(r'^$', 'index', name='index'),
    url(r'^category/(?P<slug>[-\w]+)/$', 'category'),
    url(r'^author/(?P<slug>[-\w]+)/$', 'author'),
    url(r'^document/(?P<slug>[-\w]+)/$', 'document'),
    url(r'^search/', 'search'),
)