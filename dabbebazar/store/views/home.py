from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from store.models.product import Product


@login_required
def shop_view(request):
    context = {'products': Product.objects.all}
    return render(request, 'shop.html', context)

@login_required
def cart_view(request):
    # Implement your cart logic here
    return render(request, 'cart.html')

@login_required
def checkout_view(request):
    # Implement your checkout logic here
    return render(request, 'checkout.html')