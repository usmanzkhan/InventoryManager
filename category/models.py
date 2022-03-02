from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50)
    category_description=models.TextField(max_length=255)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
       return self.category_name