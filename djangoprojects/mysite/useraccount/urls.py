from django.conf.urls import patterns, url
from useraccount import views
urlpatterns = patterns('',
url(r'^register$', views.user_register, name='user_register'),
url(r'^login$', views.user_login, name='user_login'),
url(r'^account$', views.user_account, name='user_account'),



)