from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('email', 'is_superuser', 'is_staff', 'is_landlord', 'is_tenant')
    list_filter = ('is_staff', 'is_landlord', 'is_tenant')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'is_landlord', 'is_tenant', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_landlord', 'is_tenant'),
        }),
    )

    search_fields = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
