from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    web_id = models.CharField(max_length=255)
    brand_id = models.ForeignKey("Brand", on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    color = models.ForeignKey("Color", on_delete=models.SET_NULL, null=True)
    sku = models.CharField(max_length=250, unique=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty_in_stock = models.PositiveIntegerField()
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255, unique=True)
    hex = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name