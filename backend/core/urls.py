from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductIndex.as_view()),
    path('create/products', views.CreateProduct.as_view()),
    path('signup/', views.signup),
    path('login/', views.login)
]
