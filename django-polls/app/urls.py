from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	
    #url(r'^logout/$', views.logout, name='logout'),
	url(r'^topics/$', views.topics, name='topics'),
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	url(r'^new_topic/$', views.new_topic, name='new_topic'),
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
	url(r'^clients/$', views.clients, name='clients'),
	url(r'^clients/(?P<client_id>\d+)/$', views.client, name='client'),
	url(r'^new_client/$', views.new_client, name='new_client'),
	url(r'^server/(?P<server_id>\d+)/$', views.server, name='server'),
	url(r'^new_server/(?P<client_id>\d+)/$', views.new_server, name='new_server'),
	url(r'^add_instance/(?P<server_id>\d+)/$', views.add_instance, name='add_instance'),
	url(r'^edit_server/(?P<server_id>\d+)/$', views.edit_server, name='edit_server')
	]