from django.contrib import admin
from .models import *

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price', 'quantity', 'sellers_email')
    list_filter = ('quantity', 'sellers_email')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', )

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_ordered', 'transaction_id', 'complete')
    list_filter = ('customer', 'complete')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product','quantity', 'date_added')
    list_filter = ('date_added', )

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_added')
    list_filter = ('customer', )

admin.site.site_header = "BuyAfriq"

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, StoreAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)