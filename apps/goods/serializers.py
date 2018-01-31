# -*- coding: utf-8 -*-
__author__ = 'bobby'


from rest_framework import serializers
from goods.models import Goods, GoodsCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required=True ,max_length=100)
    # click_num = serializers.IntegerField(default=0)
    # goods_front_image = serializers.ImageField()
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = "__all__"


    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Goods.objects.create(**validated_data)