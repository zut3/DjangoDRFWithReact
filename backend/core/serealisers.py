from rest_framework.serializers import ModelSerializer
from .models import Maker, Product


class MakerSerializer(ModelSerializer):

    class Meta:
        model = Maker
        fields = ['id', 'name']


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'maker']
