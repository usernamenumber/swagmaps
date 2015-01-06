from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url('proxy/(?P<url>.*)', 'proxy.views.proxy_view'),
    url('proxytest','swag.views.proxy_test'),
    url(r'^(.+)$', 'swag.views.map_view'),
    url(r'^$', 'swag.views.map_list'),
)
