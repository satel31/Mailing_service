from django.contrib import admin
from apps.clients.models import Clients, Groups

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'name', 'comment', 'group',)
    list_filter = ('comment', 'group',)
    search_fields = ('email', 'name', 'group',)

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'group_name', 'description',)
    list_filter = ('group_name',)
    search_fields = ('group_name', 'description',)
