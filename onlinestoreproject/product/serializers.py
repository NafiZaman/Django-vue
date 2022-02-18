from django.forms import ValidationError
from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('key', 'name', 'price', 'brand', 'weight', 'dimensions', 'slug',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = ('key', 'name')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('key', 'name')

class PriceRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceRange
        fields = ('key', 'min', 'max')

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        # fields = ('img', 'product',)
        fields = ['img']

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ('key', 'name')

        
# class NewProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('name', 'price', 'brand', 'weight', 'dimensions', 'slug',)

# class NewCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['name']


# class NewBrandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Brand
#         fields = ['name']

# class NewPriceRangeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PriceRange
#         fields = ('min', 'max')

#     def validate(self, data):
#         if data['max'] < data['min']:
#             raise ValidationError({'max':["max cannot be lower than min"]})
#         elif data['min'] < 500 or data['max'] < 500:
#             raise ValidationError({'data':["max or min cannot be less than 500"]})
        
#         return data

# class NewProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = ('img', 'product',)

# class NewProductCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductCategory
#         fields = ('product', 'category')
