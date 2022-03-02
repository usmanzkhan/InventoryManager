from django.forms import ModelForm
from django import forms

from .models import Product


class ProductForm(ModelForm):
    
    class Meta:
        model=Product
        fields =('product_name','product_descritption','available_quantity','threshold_quantity','product_status','category','supplier')
        
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'category_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Category Descriptiom'}),
            'is_active' : forms.CheckboxInput(),

            
        }
    