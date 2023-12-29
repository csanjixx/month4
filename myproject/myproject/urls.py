from django.urls import path
from .views import create_product, create_category, product_detail

urlpatterns = [
    path('product/create/', create_product, name='create_product'),
    path('categories/create/', create_category, name='create_category'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    # Добавьте другие URL-ы, если это необходимо
]
