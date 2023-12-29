from django import forms
from .models import Product, Category, Review

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description']

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'content']
