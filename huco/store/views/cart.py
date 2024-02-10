
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from http import HttpResponseRedirect
from ..models.products import Product

@login_required
def Cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        messages.success(request, f"{product.name} added to your cart.")
        return HttpResponseRedirect("cart:add_to_cart", product_id=product.id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
