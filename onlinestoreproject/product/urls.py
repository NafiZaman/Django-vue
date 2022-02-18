from django.urls import path
from . import views

urlpatterns = [
    path('get-all-products', views.get_all_products, name='get-all-products'),
    path('get-products-by-filter', views.get_products_by_filter, name='get-products-by-filter'),
    path('get-featured-categories', views.get_featured_categories, name='get-featured-categories'),
    path('get-filters', views.get_filters, name='get-filters'),
    path('get-product/<str:key>', views.get_product, name='get-product'),
    path('get-product-images/<str:key>', views.get_product_images, name='get-product-images'),
    # path('insert-brand', views.insert_brand, name="inser-brand"),
    # path('insert-category', views.insert_category, name="inser-category"),
    # path('insert-product', views.insert_product, name="insert-product"),
    # path('insert-product-image', views.insert_product_image, name="insert-product-image"),
    # path('insert-price-range', views.insert_price_range, name="insert-price-range"),
    # path('insert-product-category', views.insert_product_category, name="insert-product-category"),
]
