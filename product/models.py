from django.db import models

from category.models import Category
from supplier.models import Supplier

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_description=models.CharField(max_length=255)
    available_quantity=models.IntegerField()
    threshold_quantity=models.IntegerField()
    product_status=models.BooleanField(default=True)
    category=models.OneToOneField(Category,on_delete=models.CASCADE,primary_key=True)
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name