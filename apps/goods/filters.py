# -*- coding: utf-8 -*-
__author__ = 'bobby'

#from rest_framework import generics
#from django_filters import rest_framework as filters
import django_filters

from .models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品d过滤
    """
    min_price = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    name = django_filters.CharFilter(name='name')

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price','name']
