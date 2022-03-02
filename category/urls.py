from django.urls import path
from . import views

urlpatterns = [
    path('',views.category,name='category'),
    path('create_category/',views.create_category,name='create_category'),
    path('edit_category/<int:pk>/',views.edit_category,name='edit_category'),
    path('delete_category/<int:pk>/',views.delete_category,name='delete_category'),
]