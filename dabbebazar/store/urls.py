from django.urls import path
from .views.api import category_detail_view, category_view, cart_detail_view, product_detail_view, product_view ,add_to_cart_view

app_name = 'store'
from django.urls import path
from .views import login_view, register_view , forgot_password_view, shop_view, cart_view, checkout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    # path('dashboard/', dashboard_view, name='dashboard'),
    path('shop/', shop_view, name='shop'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    
    path('categories/', category_view),
    path('categories/<int:pk>/', category_detail_view),
    
    path('products/', product_view),
    path('products/<int:pk>/', product_detail_view),

    path('carts/add/', add_to_cart_view),
    path('carts/<int:pk>/', cart_detail_view),
]