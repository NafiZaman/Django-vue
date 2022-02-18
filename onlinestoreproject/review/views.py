from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import *
from .models import *

@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_reviews(request, prod_key):
    revs = Review.objects.filter(product_id__key=prod_key)
    revs_ser = ReviewSerializer(revs, many=True)

    return Response(revs_ser.data)