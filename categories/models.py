from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Model representing Category table implemented with MPTT."""
    name = models.CharField(
        max_length=250,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("category name")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("is category active")
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_("parent of category")
    )

    class MPTTMeta:
        order_insertion_by = ['name']
    
    class Meta:
        db_table = 'categories'
        managed = True
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")

    def __str__(self) -> str:
        return f"{self.name}"
