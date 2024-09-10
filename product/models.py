from distutils.command import upload
from django.db import models

import uuid
from account.models import *

from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=12)
    product_image = models.ImageField(upload_to="products/", default="products/default-product.png", null=True, blank=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.CharField(max_length=50, null=True, blank=True, unique=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
    
    def save(self, *args, **kwargs):
        if not self.product_id:
            self.product_id = str(uuid.uuid4()).replace('-', "").upper()[:10]
        return super().save(*args, **kwargs)
    

class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product, related_name="cart")
    total_amount = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=12)

    def get_total_amount(self):
        total = Decimal(0)
        for product in self.products.all():
            total += product.price
        return total