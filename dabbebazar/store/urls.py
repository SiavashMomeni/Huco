from django.urls import path
from .views import category_detail_view, category_view, cart_detail_view, product_detail_view, product_view ,add_to_cart_view

app_name = 'store'

urlpatterns = [
    path('categories/', category_view),
    path('categories/<int:pk>/', category_detail_view),
    
    path('products/', product_view),
    path('products/<int:pk>/', product_detail_view),

    path('carts/add/', add_to_cart_view),
    path('carts/<int:pk>/', cart_detail_view),
]