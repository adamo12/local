from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
       # Login page
    url(r'^login/$', login, {'template_name':'users/login.html'}, name='login'),
	url(r'^logout/$', logout, {'template_name':'users/logout.html'}, name='logout'),
   ]