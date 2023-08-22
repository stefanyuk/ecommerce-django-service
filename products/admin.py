from django.contrib import admin

from .models import Product, Brand, Color


admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Color)