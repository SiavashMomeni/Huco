from .models.category import Category
from rest_framework import serializers
from .models.product import Product
from .models.cart import CartItem
from django.contrib.auth.models import User





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = ['id', 'name', 'category', 'price']

  
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = CartItem 
        fields = ['id', 'product', 'quantity', 'total_price']

class CartSerializer(serializers.ModelSerializer):   
    items = CartItemSerializer(many=True)  
    total = serializers.SerializerMethodField()
    
    def get_total(self, cart):
        return sum(item.total_price for item in cart.items.all())