from dataclasses import fields
from django.forms import ModelForm
from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
    
        fields = ('supplier_name','supplier_address','supplier_email','is_active')
        
        widgets = {
            'supplier_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supplier Name'}),
            'supplier_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Supplier Address'}),
            'supplier_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supplier Email'}),
            'is_active' : forms.CheckboxInput(),

            
        }

