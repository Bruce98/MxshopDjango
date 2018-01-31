from django.shortcuts import render
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response



from .serializers import GoodsSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods
# Create your views here.


class GoodsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        goods = Goods.objects.[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)