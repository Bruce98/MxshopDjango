from rest_framework import serializers


class GoodsSerializer(serializers):
    name = models.CharField(required=True ,max_length=100)
    click_num = serializers.IntegerField(default=0)