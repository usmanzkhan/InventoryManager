from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.suppliers,name='supplier'),
    path('create_supplier/',views.create_supplier,name='create_supplier'),
    path('edit_supplier/<int:pk>/',views.edit_supplier,name='edit_supplier'),
    path('delete_supplier/<int:pk>/',views.delete_supplier,name='delete_supplier')
]
