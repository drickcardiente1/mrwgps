from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from django.contrib import admin

class Usersclient(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'last_login','type')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_client',
        )}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_admin', 'last_login','type')
    search_fields = ('email', 'username',)
    ordering = ('email', 'username',)
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(client,Usersclient)