from rest_framework import generics
from .serealisers import MakerSerializer, ProductSerializer
from . import models


class ProductIndex(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return models.Product.objects.all()


class MakerIndex(generics.ListAPIView):
    serializer_class = MakerSerializer

    def get_queryset(self):
        return models.Maker.objects.all()


class CreateProduct(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return models.Product.objects.all()


class CreateMaker(generics.CreateAPIView):
    serializer_class = MakerSerializer

    def get_queryset(self):
        return models.Maker.objects.all()


