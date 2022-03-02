from django.db import models

# Create your models here.

class Supplier(models.Model):
    supplier_name=models.CharField(max_length=50)
    supplier_address=models.CharField(max_length=255)
    supplier_email=models.EmailField()
    is_active=models.BooleanField(default=False)
    
    def __str__(self):
        return self.supplier_name
    
