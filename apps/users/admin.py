from django.contrib import admin

from apps.users.models import User


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'activation_code', 'password', 'is_activated')

    def get_readonly_fields(self, request, obj=None):
        """Makes fields readonly"""
        if request.user.is_superuser:
            return self.readonly_fields
        else:
            return ['email', 'activation_code', 'password', 'last_login', 'is_superuser', 'groups', 'user_permissions',
                    'first_name', 'last_name', 'is_staff', 'date_joined']
