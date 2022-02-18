# from rest_framework.views import APIView
# from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Avg

from .serializers import *
from .models import *
from review.models import Review

import json
# import re

def get_product_data(products):
    prod_ser = ProductSerializer(products, many=True)
    product_data = []
    
    for d in prod_ser.data:
        data = {}
        data = d        
        data['image'] = ProductImage.objects.filter(product_id=d['name']).values_list('img', flat=True).first()
        data['avg_rating'] = Review.objects.filter(product_id=d['name']).aggregate(Avg('rating'))['rating__avg']
        product_data.append(data)

    return product_data

@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_all_products(request):
    products = Product.objects.all()
    product_data = get_product_data(products)

    return Response(product_data)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_products_by_filter(request):
    params = json.loads(request.query_params.dict()['params'])
    # print(params, "\n")
    # print(len(params))

    if len(params) > 0:
        avail_prods = []
        cat_prods = []
        brand_prods = []
        price_prods = []

        if 'availability' in params:
            avail_prods=list(Stock.objects.filter(quantity__gt=0).values_list('product_id', flat=True))
        if 'category' in params:
            cat_prods = list(ProductCategory.objects.filter(category_id__key__in=params['category']).values_list('product_id', flat=True))
        if 'brands' in params:
            brand_prods = list(Product.objects.filter(brand_id__key=params['brands']).values_list('name', flat=True))
        if 'price' in params:
            price_range = list(PriceRange.objects.filter(key=params['price']).values_list('min', 'max')[0])
            price_prods = list(Product.objects.filter(price__gte=price_range[0], price__lte=price_range[1]).values_list('name', flat=True))
            # print(price_range)

        result_set = list(set.intersection(*(set(x) for x in [avail_prods, cat_prods, brand_prods, price_prods] if x)))
        products = Product.objects.filter(name__in=result_set)
    else:
        products = Product.objects.all()

    product_data = get_product_data(products)
    return Response(product_data)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_featured_categories(request):
    max_categories = 6
    categories = Category.objects.order_by('?')[:max_categories]
    category_serializer = CategorySerializer(categories, many=True)
    featured_data = []
    for cs in category_serializer.data:
        product = ProductCategory.objects.filter(category_id = cs['name']).values_list('product_id', flat=True)[0]
        product_image = ProductImage.objects.filter(product_id=product).values_list('img', flat=True)[0]

        data = cs
        data['name'] = cs['name']
        data['image'] = product_image
        featured_data.append(data)

    return Response(featured_data)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_filters(request):
    data = {}
    
    availability_serializer = AvailabilitySerializer(Availability.objects.all(), many=True)
    data['availability'] = availability_serializer.data

    category_serializer = CategorySerializer(Category.objects.all().order_by('name'), many=True)
    data['category'] = category_serializer.data

    brand_serializer = BrandSerializer(Brand.objects.all().order_by('name'), many=True)
    data['brands'] = brand_serializer.data

    price_rage_serializer = PriceRangeSerializer(PriceRange.objects.all().order_by('pk'), many=True)
    data['price'] = price_rage_serializer.data

    return Response(data)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_product(request, key):
    prod = Product.objects.get(key=key)
    prod_ser = ProductSerializer(prod, many=False)
    data = {}
    data = prod_ser.data
    data['category'] = ProductCategory.objects.filter(product=prod).values_list('category', flat=True)
    data['avg_rating'] = Review.objects.filter(product=prod).aggregate(Avg('rating'))['rating__avg']

    return Response(data)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_product_images(request, key):
    img_ser = ProductImageSerializer(ProductImage.objects.filter(product_id__key=key), many=True)

    return Response(img_ser.data)


# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def insert_brand(request):
#     serializer = NewBrandSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, 200)
#     else:
#         return Response(serializer.errors, 500)

# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def insert_category(request):
#     serializer = NewCategorySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, 200)
#     else:
#         return Response(serializer.errors, 500)

# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def insert_product(request):
#     serializer = NewProductSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, 200)
#     else:
#         return Response(serializer.errors, 500)

# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def insert_product_image(request):
#     serializer = NewProductImageSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, 200)
#     else:
#         return Response(serializer.errors, 500)

# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def insert_price_range(request):
#     serializer = NewPriceRangeSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, 200)
#     else:
#         return Response(serializer.errors, 500)


# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def insert_product_category(request):
#     serializer = NewProductCategorySerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, 200)
#     else:
#         return Response(serializer.errors, 500)