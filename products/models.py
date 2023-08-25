from django.db import models
from uuid import uuid4

MIN_QTY_IN_STOCK = 0


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    web_id = models.CharField(verbose_name="web display id", max_length=255, default=uuid4)
    brand = models.ForeignKey("Brand", on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    color = models.ForeignKey("Color", verbose_name="color", on_delete=models.SET_NULL, null=True)
    sku = models.CharField(verbose_name="stock keeping unit", max_length=250, unique=True)
    sale_price = models.DecimalField(verbose_name="selling price", max_digits=10, decimal_places=2)
    stock_price = models.DecimalField(verbose_name="stock price", max_digits=10, decimal_places=2)
    qty_in_stock = models.PositiveIntegerField(verbose_name="available quantity", default=MIN_QTY_IN_STOCK)
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE)
    released_on = models.DateField(verbose_name="release year")
    warranty_period_in_months = models.PositiveIntegerField()
    weight = models.DecimalField(verbose_name="weight", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f"{self.name} {self.sku}"

    def is_available(self):
        return self.qty_in_stock > MIN_QTY_IN_STOCK
    
    def get_field_title(self):
        pass


class Color(models.Model):
    name = models.CharField(max_length=255, unique=True)
    hex = models.CharField(max_length=255, unique=True)
    
    class Meta:
        db_table = 'colors'
        verbose_name = 'color'
        verbose_name_plural = 'colors'
    
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    class Meta:
        db_table = 'brands'
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
    
    def __str__(self):
        return self.name