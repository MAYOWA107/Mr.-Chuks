from django.contrib import admin

from .models import Order, OrderFood, Cart, CartFood


admin.site.register(Order)
admin.site.register(OrderFood)
admin.site.register(Cart)
admin.site.register(CartFood)
