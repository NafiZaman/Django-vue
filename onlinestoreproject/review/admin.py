from django.contrib import admin
from .models import Review

class ReviewAdminConfig(admin.ModelAdmin):
    search_fields = ['product',]
    ordering = ("-title",)
    list_display = ("product", 'title', 'user')

    fieldsets = (
        ('Product Information', {'fields': ('product', 'title', 'text', 'rating', 'user', 'date_posted',)}),
    )
    

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

admin.site.register(Review, ReviewAdminConfig)