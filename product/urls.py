from re import I
from django import views
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.product, name='product'),
    path('create_product/',views.create_product,name='create_product')
]
