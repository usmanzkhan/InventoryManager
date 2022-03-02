import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

def product(request):
    
    products=Product.objects.all()
    context={'products': products}
    return render(request,'product/index.html',context)


def create_product(request):
    form=ProductForm()
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.save():
            return redirect('product')
    context ={'form':form}
    return render(request,'product/create_product.html',context)

# Create your views here.
