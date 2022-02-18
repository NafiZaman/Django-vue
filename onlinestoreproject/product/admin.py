from encodings import search_function
from django.contrib import admin

from .models import *

class ProductAdminConfig(admin.ModelAdmin):
    search_fields = ['name',]
    ordering = ("-name",)
    list_display = ('name', 'price', 'brand',)

    fieldsets = (
        ('Product Information', {'fields': ('name', 'price', 'brand', 'weight', 'dimensions', 'slug')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'price', 'brand', 'weight', 'dimensions',),
        }),
    )

    # def has_delete_permission(self, request, obj=None):
    #     return False

class ProductCategoryAdminConfig(admin.ModelAdmin):
    search_fields = ['product',]
    ordering = ("-product",)
    list_display = ('product', 'category',)

class StockAdminConfig(admin.ModelAdmin):
    search_fields = ['product',]
    ordering = ("-product",)
    list_display = ('product', 'quantity',)

    fieldsets = (
        ('Stock Information', {'fields': ('product', 'quantity',)}),
    )

    def has_add_permission(self, request, obj=None):
        return False
    
    # def has_delete_permission(self, request, obj=None):
    #     return False

class CategoryAdminConfig(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ('name',)
    list_display = ('name',)

class ProductImageAdminConfig(admin.ModelAdmin):
    search_fields = ['product__name',]
    ordering = ('product',)
    list_display = ('product', 'img')

class PriceRangeAdminConfig(admin.ModelAdmin):
    list_display = ('key', 'min', 'max')

admin.site.register(Product, ProductAdminConfig)
admin.site.register(Brand)
admin.site.register(ProductCategory, ProductCategoryAdminConfig)
admin.site.register(Stock, StockAdminConfig)
admin.site.register(Category, CategoryAdminConfig)
admin.site.register(ProductImage, ProductImageAdminConfig)
admin.site.register(PriceRange, PriceRangeAdminConfig)
admin.site.register(Availability)