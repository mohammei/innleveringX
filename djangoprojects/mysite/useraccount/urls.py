from django.conf.urls import patterns, url
from useraccount import views
urlpatterns = patterns('',
url(r'^register$', views.user_register, name='user_register'),
)