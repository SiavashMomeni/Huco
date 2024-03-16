from django.db import models
from django.core import serializers
from .category import Category
from .product import Product



class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  
    status = models.CharField(max_length=20, choices=[
        ('OPEN', 'Open'), 
        ('CHECKOUT', 'Checkout'),
    ])
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    quantity = models.IntegerField()
    
    @property
    def total_price(self):
        return self.quantity * self.product.price 
