from django.contrib import admin

from app.models import Topic, Entry, Client, Server, Instance

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Client)
admin.site.register(Server)
admin.site.register(Instance)

