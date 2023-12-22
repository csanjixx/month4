from django.shortcuts import render
from .models import Category

def categories_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'categories.html', context)
