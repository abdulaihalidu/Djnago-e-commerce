from django.contrib import admin
from .models import *

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Customer)
admin.site.register(Product, StoreAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)