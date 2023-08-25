from django.db import models
from django.db.models import F
from django.utils.translation import gettext_lazy as _
from mptt.models import TreeManyToManyField
from uuid import uuid4
from django.db.models.query import QuerySet


COLOR_ATTRIBUTE_NAME = "Color"

class Product(models.Model):
    """Model representing Product table."""
    web_id = models.CharField(
        max_length=36,
        unique=True,
        null=False,
        blank=False,
        default=uuid4,
        verbose_name=_("product website ID")
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("product name"),
        help_text=_("format: required, max-255"),
    )
    description = models.TextField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("product description")
    )
    category = TreeManyToManyField("categories.Category", related_name="products")
    brand = models.ForeignKey(
        "Brand", related_name="products", on_delete=models.PROTECT
    )
    is_active = models.BooleanField(
        unique=False,
        null=False,
        blank=False,
        default=True,
        verbose_name=_("is product active")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date product last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = _("product")
        verbose_name_plural = _("products")


class Brand(models.Model):
    """Model representing product brand table."""
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("brand name")
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = 'brands'
        verbose_name = _("product brand")
        verbose_name_plural = _("product brands")


class ProductType(models.Model):
    """Model representing product type table."""
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("type of product")
    )
    product_attributes = models.ManyToManyField(
        "ProductAttribute",
        through="ProductTypeAttribute",
        related_name="product_types"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product_types'
        verbose_name = _("product type")
        verbose_name_plural = _("product types")


class ProductAttribute(models.Model):
    """Model representing product attribute table."""
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("product attribute name")
    )
    information_tag = models.TextField(
        unique=False,
        null=False,
        blank=True,
        verbose_name=_("product attribute information tag")
    )
    label = models.ForeignKey(
        "Label",
        on_delete=models.SET_NULL,
        related_name="product_attributes",
        null=True,
        blank=False
    )
    icon = models.ImageField(
        verbose_name=_("product attribute icon"),
        upload_to="icons/product-attribute/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_attributes'
        verbose_name = _("product attribute")
        verbose_name_plural = _("product attribute")


class Label(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("product attribute label")
    )

    class Meta:
        db_table = 'labels'
        verbose_name = _("attribute label")
        verbose_name_plural = _("attribute lables")
    
    def __str__(self) -> str:
        return f"{self.name}"


class ProductAttributeValue(models.Model):
    """Model representing product attribute value table."""
    product_attribute = models.ForeignKey(
        "ProductAttribute",
        related_name="attribute_values",
        on_delete=models.PROTECT,
    )
    value = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("attribute value")
    )

    def __str__(self):
        return f"{self.product_attribute.name}: {self.value}"
    
    class Meta:
        db_table = 'product_attribute_values'
        verbose_name = _("product attribute value")
        verbose_name_plural = _("product attribute values")


class ProductItemManager(models.Manager):
    def get_sibling_product_items(self, product_item: "ProductItem") -> QuerySet["ProductItem"]:
        return self.filter(product=product_item.product).prefetch_related("attribute_values")


class ProductItem(models.Model):
    """Model representing product item table."""
    sku = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("stock keeping unit")
    )
    qty_in_stock = models.PositiveIntegerField(default=0)
    product_type = models.ForeignKey(
        "ProductType", related_name="product_items", on_delete=models.PROTECT
    )
    product = models.ForeignKey(
        "Product", related_name="product_items", on_delete=models.PROTECT
    )
    attribute_values = models.ManyToManyField(
        "ProductAttributeValue",
        related_name="product_items",
        through="ProductItemAttributeValue"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("product visibility"),
        help_text=_("format: true=product visible"),
    )
    sale_price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("sale price"),
        help_text=_("format: maximum price 999999999.99"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999999999.99."),
            },
        },
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date sub-product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date sub-product updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    
    objects = ProductItemManager()

    def __str__(self):
        return f"{self.product.name}({self.sku})"

    class Meta:
        db_table = 'product_items'
        verbose_name = _("product item")
        verbose_name_plural = _("product items")

    @property
    def highlighted_attributes(self):
        return self.attribute_values.filter(
            attribute_value_item_config__to_highlight=True
        ).annotate(
            label=F("product_attribute__name"), icon_url=F("product_attribute__icon")
        )

    @property
    def color(self) -> ProductAttributeValue:
        return self.attribute_values\
            .filter(
                product_attribute__is_common=False,
                product_attribute__name=COLOR_ATTRIBUTE_NAME
            )\
            .first()

    @property
    def display_name(self):
        parts_of_the_name = [self.product.name]
        
        non_common_attributes = self.get_non_common_attributes()
        
        for attr in non_common_attributes:
            parts_of_the_name.append(attr.value)
        
        parts_of_the_name.append(f"({self.sku})")

        return " ".join(parts_of_the_name)

    def get_non_color_attributes(self) -> QuerySet:
        return self.attribute_values\
            .select_related("product_attribute")\
            .exclude(
                product_attribute__name=COLOR_ATTRIBUTE_NAME
            )

    def get_non_common_attributes(self) -> QuerySet:
        return self.attribute_values\
            .select_related("product_attribute")\
            .filter(
                product_attribute__product_type_configuration__is_common=False
            )

    def get_attributes(self) -> QuerySet:
        return self.attribute_values.select_related("product_attribute").all()


class Media(models.Model):
    """Model representing media table, that contains media data related to product item images."""
    product_item = models.ForeignKey(
        "ProductItem",
        on_delete=models.PROTECT,
        related_name="media"
    )
    image = models.ImageField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product image"),
        upload_to="images/product-item/",
        default="images/default.png"
    )
    alt_text = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("alternative text")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("product visibility"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date sub-product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        db_table = "medias"
        verbose_name = _("product image")
        verbose_name_plural = _("product images")


class ProductTypeAttribute(models.Model):
    product_attribute = models.ForeignKey(
        "ProductAttribute",
        on_delete=models.CASCADE,
        related_name="product_type_configuration"
    )
    product_type = models.ForeignKey(
        "ProductType",
        on_delete=models.CASCADE,
        related_name="product_type_configuration"
    )
    display_order = models.PositiveIntegerField(null=False, blank=False)
    is_common = models.BooleanField(default=True)

    class Meta:
        db_table = "product_types_attributes"
        verbose_name = _("type and attribute")
        verbose_name_plural = "types and attributes"
        unique_together = ["product_attribute", "product_type"]

    def __str__(self) -> str:
        return f"{self.product_type.name}: {self.product_attribute.name} ({self.sequence})"


class ProductItemAttributeValue(models.Model):
    attribute_value = models.ForeignKey(
        "ProductAttributeValue",
        on_delete=models.CASCADE,
        related_name="product_attr_configuration"
    )
    product_item = models.ForeignKey(
        "ProductItem",
        on_delete=models.CASCADE,
        related_name="product_attr_configuration"
    )
    to_highlight = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_items_attribute_values'
        verbose_name = 'product item attribute value'
        verbose_name_plural = 'product items attribute values'
        unique_together = ["attribute_value", "product_item"]

    def __str__(self) -> str:
        return f"{self.product_item.product.name}({self.product_item.sku}): {self.attribute_value.value}"
