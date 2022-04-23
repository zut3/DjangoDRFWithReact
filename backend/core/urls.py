from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductIndex.as_view()),
    path('makers', views.MakerIndex.as_view()),
    path('create/products', views.CreateProduct.as_view()),
    path('create/makers', views.CreateMaker.as_view())
]
