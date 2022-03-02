from django.shortcuts import redirect, render
from django.http import HttpResponse
from category.views import category

from supplier.models import Supplier
from .forms import SupplierForm

# Create your views here.

def suppliers(request):
    suppliers=Supplier.objects.all()
    return render(request,'supplier/index.html',{'suppliers':suppliers})

def create_supplier(request):
    
    form=SupplierForm()
    if request.method == 'POST':
        form=SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('supplier')      
    context= {'form':form,}
    return render(request,'supplier/create_supplier.html',context)

def edit_supplier(request,pk):
    supplier=Supplier.objects.get(id=pk)
    form=SupplierForm(instance=supplier)
    if request.method == 'POST':
        form=SupplierForm(request.POST,instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier')
    context= {'form':form,}
    return render(request,'supplier/edit_supplier.html',context)

def delete_supplier(request,pk):
    supplier=Supplier.objects.get(id=pk)
  
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier')
    context= {'supplier':supplier,}
    return render(request,'supplier/delete_supplier.html',context)
