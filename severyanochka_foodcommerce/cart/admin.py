from django.contrib import admin
from .models import Order, OrderItem, CartItem, Cart
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)

