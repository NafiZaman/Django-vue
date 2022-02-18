from ast import Return
from rest_framework import response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import *
from .serializers import AccountSerializer, NewAccountSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    # print(request)
    serializer = NewAccountSerializer(data=request.data)
    # print(request.data)

    data = {}
    if serializer.is_valid():
        newaccount = serializer.save()
        data = serializer.data
        try:
            token = Token.objects.get(user=newaccount).key
        except Exception as e:
            return Response(serializer.errors, 500)
        data['token'] = token
        return Response(data, 200)
    else:
        return Response(serializer.errors, 400)

@api_view(['POST'])
def log_out(request):
    try:
        request.user.auth_token.delete()
        return Response("User has been logged out")
    except Exception as e:
        print(e)

    return Response("An error occured")

@api_view(['GET'])
def get_user_profile(request):
    # print(request.user.auth_token)
    # print(request.user)
    try:
        account_ser = AccountSerializer( Account.objects.get(username=request.user), many=False)
    except Exception as e:
        print(e)

    return Response(account_ser.data)