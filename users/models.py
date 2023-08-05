from django.db import models

# Create your models here.


class Product(models.Model):
    product_image = models.ImageField(null=True, blank=True, upload_to="images/")