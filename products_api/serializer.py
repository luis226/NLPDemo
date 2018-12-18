from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'created_date')


class DialogFlowRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DialogFlowRequest
        fields = ('created_date', 'content')
