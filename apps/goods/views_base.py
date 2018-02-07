# -*- coding: utf-8 -*-
__author__ = 'bobby'

from goods.models import Goods
from django.views.generic.base import View
from django.views.generic import ListView
    

 
class GoodsListView(View):
    def get(self,request):
        """
        通过django实现View
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.category.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     json_list.append(json_dict)


        # from django.forms.models import  model_to_dict    
        # for good in goods:
        # 	json_dict = model_to_dict(good)
        # 	json_list.append(json_dict)d

        import json
        from django.core import serializers
        json_data = serializers.serialize("json",goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse,JsonResponse
        return JsonResponse(json_data,safe=False)
        
       