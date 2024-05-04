from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin


from django.contrib import admin
from .models import Product,CartItem,BillingDetails,Order,OrderItem

admin.site.register(Product)

admin.site.register(CartItem)

admin.site.register(BillingDetails)

admin.site.register(Order)

admin.site.register(OrderItem)
