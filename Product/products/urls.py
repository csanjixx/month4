from django.urls import path
from .views import main_view, products_view, categories_view

urlpatterns = [
    path('', main_view, name='main_view'),
    path('products/', products_view, name='products_view'),
    path('categories/', categories_view, name='categories_view'),
]
