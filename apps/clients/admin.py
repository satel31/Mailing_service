from django.contrib import admin
from apps.clients.models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'last_name', 'comment',)
    list_filter = ('comment',)
    search_fields = ('email', 'first_name', 'last_name',)



