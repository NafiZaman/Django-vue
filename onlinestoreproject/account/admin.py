from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdminConfig(UserAdmin):
    search_fields = ['username', 'email']
    ordering = ("-username",)
    list_display = ('username', 'email','is_superuser',)

    fieldsets = (
        ('User Information', {'fields': ('username', 'email',)}),
        # ('User Information', {'fields': ('username', 'email', 'password')}),

        # ('Permissions', {
        #  'fields': ('is_superuser', 'is_staff', 'is_active',)}),
        ('Other Information', {'fields': ('first_name', 'last_name', 'last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',),
        }),
    )

    def has_change_permission(self, request, obj=None):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

admin.site.register(Account, AccountAdminConfig)

# Register your models here.
