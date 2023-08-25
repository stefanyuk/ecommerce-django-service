from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name