from random import choices
from django.forms import ModelForm
from django import forms

from .models import Product
from category.models import Category
from supplier.models import Supplier


class ProductForm(ModelForm):
    product_name=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'})
    category=forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
       
        model=Product
        fields =('product_name','category')
        
       
    