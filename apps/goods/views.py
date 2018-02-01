# -*- coding: utf-8 -*-
__author__ = 'bobby'



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from .models import Goods,GoodsCategory
from .serializers import GoodsSerializer,CategorySerializer 

from .filters import GoodsFilter
# Create your views here.

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class GoodsListViewsets(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    商品列表,分页，搜索，过滤，排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief','goods_desc')
    Ordering_filter = ('sold_num','add_time','shop_price')
    

class CategoryViewsets(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    List:
        商品分类列表
    """

    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer



# class GoodsListView(generics.ListAPIView):
#     """
#    商品列表
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = LargeResultsSetPagination

    
# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
#     """
#    商品列表
#     """
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)




    # def get(self, request, format=None):
    #     goods = Goods.objects.all()[:10]
    #     goods_serializer = GoodsSerializer(goods, many=True)
    #     return Response(goods_serializer.data)


    # def post(self, request, format=None):
    #     serializer = GoodsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)