
from . models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    search_fields = ['email', ]
    ordering = ("-email",)
    list_display = ('email', 'is_superuser',
                    'is_staff', 'is_active',)

    fieldsets = (
        ('User Information', {'fields': ('email', 'password',)}),

        ('Permissions', {
         'fields': ('is_superuser', 'is_staff', 'is_active',)}),
        ('Other Information', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
    )


admin.site.register(NewUser, UserAdminConfig)
