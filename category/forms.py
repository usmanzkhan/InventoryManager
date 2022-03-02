
from django import forms
from django.forms import ModelForm
from .models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
    
        fields =('category_name','category_description','is_active')
        
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'category_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Category Descriptiom'}),
            'is_active' : forms.CheckboxInput(),

            
        }