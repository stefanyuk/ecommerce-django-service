from django.contrib import admin

from . import models

admin.site.register(models.Product)
admin.site.register(models.ProductAttribute)
admin.site.register(models.ProductAttributeValue)
admin.site.register(models.ProductType)
admin.site.register(models.Brand)
admin.site.register(models.ProductItem)
admin.site.register(models.Media)
admin.site.register(models.Label)
admin.site.register(models.ProductTypeAttribute)
