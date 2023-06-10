from django.contrib import admin
from apps.clients.models import Clients

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'name', 'comment',)
    list_filter = ('comment',)
    search_fields = ('email', 'name',)



