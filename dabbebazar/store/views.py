from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from store.models import Cart, CartItem, Category, Customer, Product

from .serializers import ProductSerializer, CartSerializer, CategorySerializer



@api_view(['GET', 'POST'])
def category_view(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data) 

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_view(request, pk):

    try: 
        category = Category.objects.get(pk=pk) 
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def product_view(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, pk):
    
    try:
        product = Product.objects.get(pk=pk) 
    except Product.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method in ['PUT', 'PATCH']:
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
@api_view(['POST'])
def add_to_cart_view(request):

    data = request.data
    product_id = data['product_id']
    quantity = data['quantity']
    
    try:
        # Get product instance  
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
     
    # Check if user has an open cart 
    cart, created = Cart.objects.get_or_create(user=request.user, status='OPEN')
    
    # Create or update cart item 
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, 
        product=product,
        defaults={'quantity': quantity}
    )
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
        
    # Recalculate cart totals
    total_price = 0  
    items = cart.cartitem_set.all()
    for item in items:
        total_price += item.quantity * item.product.price 
    
    cart.total_price = total_price
    cart.save()
    
    # Return updated cart data
    serializer = CartSerializer(cart)
    return Response(serializer.data)
    

@api_view(['GET'])
def cart_detail_view(request, pk):

    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CartSerializer(cart)
    return Response(serializer.data)

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Cart, CartItem 
from .serializers import ProductSerializer, CartSerializer


@api_view(['GET', 'POST'])
def product_view(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, pk):
    
    try:
        product = Product.objects.get(pk=pk) 
    except Product.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method in ['PUT', 'PATCH']:
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

@api_view(['GET'])
def cart_detail_view(request, pk):

    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CartSerializer(cart)
    return Response(serializer.data)   