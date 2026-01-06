from django.db import models
from django.contrib.auth.models import User


# PRODUCT MODEL
class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default =1)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/product/', blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
