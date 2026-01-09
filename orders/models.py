from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# from accounts.models import User

# Create your models here.

class Order(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=255, default='', blank=True)
    phone = models.CharField(max_length=12, default='', blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(max_length=50, default='False', blank=True)

    def __str__(self):
        return self.product
    