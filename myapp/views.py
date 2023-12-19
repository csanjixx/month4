from django.shortcuts import render
from .models import Product

def main_view(request):
    return render(request, 'layouts/main.html')

def products_view(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})
