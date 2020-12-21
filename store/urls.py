from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart', views.cart, name='cart'),
    path('update_item', views.updateItem, name='update_item'),
    path('checkout', views.checkout, name='checkout'),
    path('payment_order', views.payment_order, name='payment_order'),
]
