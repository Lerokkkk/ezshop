from django.urls import path, include
from .views import ShopCartViewSet
from rest_framework import routers

shop_cart_list = ShopCartViewSet.as_view({
    'get': 'list'
})

shop_cart_detail = ShopCartViewSet.as_view({
    'post': 'create',
    'delete': 'destroy'
})

urlpatterns = [
    path('shop-cart/', shop_cart_list, name='shop-cart-list'),
    path('shop-cart/<int:game_id>/', shop_cart_detail, name='shop-cart-detail'),
]
