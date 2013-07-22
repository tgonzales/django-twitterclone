from django.conf.urls import patterns, include, url
from .views import HomeView, HomeTwitts, UserCreateView, UserStatusView

urlpatterns =  patterns('',
	url(r'^$', HomeTwitts.as_view(), name='home'),
    url(r'^adduser/$', UserCreateView.as_view(), name='add-user'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'twitter/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, 'logout'),
    url(r'^status/$', UserStatusView.as_view(), name='status'),


)