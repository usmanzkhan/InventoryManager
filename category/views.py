import re
from django.shortcuts import redirect, render
from django.http import HttpResponse

from category.forms import CategoryForm
from .models import Category

# Create your views here.

def category(request):
    categories=Category.objects.all()
    context= {'categories': categories}
    return render(request, 'category/index.html',context)

def create_category(request):
    form=CategoryForm()
    
    if request.method == 'POST':
        form =CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    context= {'form':form,}
    return render(request,'category/create_category.html',context)

def edit_category(request,pk):
    category=Category.objects.get(id=pk)
    form=CategoryForm(instance=category)
    if request.method == 'POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    context={'form': form,}
    return render(request, 'category/edit_category.html',context)

def delete_category(request,pk):
    category=Category.objects.get(id=pk)
    if request.method == 'POST':
        
        category.delete()
        return redirect('category')
    context={'category': category,}
    return render(request, 'category/delete_category.html',context)