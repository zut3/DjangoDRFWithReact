from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponseNotFound
from .serealisers import ProductSerializer
from . import models


@csrf_exempt
def login(request):
    json_parser = JSONParser()
    if request.method == 'POST':
        data = json_parser.parse(request)
        user = authenticate(request,
                            username=data['username'],
                            password=data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return JsonResponse({
                'token': str(token)
            })
        return JsonResponse({"error": f"Doesn't matched user with name {data['username']}"})
    return HttpResponseNotFound()

@csrf_exempt
def signup(request):
    json_parser = JSONParser()
    if request.method == 'POST':
        try:
            data = json_parser.parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({
                'token': str(token)
            }, status=200)

        except Exception as ex:
            return JsonResponse({'error': str(ex)}, status=400)

    return HttpResponseNotFound()


class ProductIndex(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return models.Product.objects.all()


class CreateProduct(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Product.objects.filter(maker=self.request.user)

    def perform_create(self, serializer):
        serializer.save(maker=self.request.user)

