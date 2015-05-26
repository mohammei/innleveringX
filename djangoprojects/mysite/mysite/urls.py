from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #urlen for theme homepage, useraccout, post legges her
    url(r'^$', include('theme.urls')),
    url(r'^useraccount/', include('useraccount.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
