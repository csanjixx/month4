from django.shortcuts import render, redirect
from .models import Product, Category, Review
from .forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm

def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=form.instance.pk)
    else:
        form = ProductCreateForm()
    return render(request, 'product/create.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Или куда вы хотите перенаправить после создания категории
    else:
        form = CategoryCreateForm()
    return render(request, 'categories/create.html', {'form': form})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        review_form = ReviewCreateForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.product = product
            new_review.save()
            return redirect('product_detail', pk=pk)
    else:
        review_form = ReviewCreateForm()

    return render(request, 'product/detail.html', {'product': product, 'reviews': reviews, 'review_form': review_form})
