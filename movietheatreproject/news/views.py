from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import News
from .serializers import NewsSerializer


@api_view(['GET'])
def get_news(request):
    news = News.objects.all()
    news_serializer = NewsSerializer(news, many=True)

    return Response(news_serializer.data)
