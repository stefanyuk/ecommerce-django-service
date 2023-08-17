# Generated by Django 4.2.4 on 2023-08-17 10:43

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="brand name"
                    ),
                ),
            ],
            options={
                "verbose_name": "product brand",
                "verbose_name_plural": "product brands",
                "db_table": "brands",
            },
        ),
        migrations.CreateModel(
            name="Label",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        verbose_name="product attribute label",
                    ),
                ),
            ],
            options={
                "verbose_name": "attribute label",
                "verbose_name_plural": "attribute lables",
                "db_table": "labels",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "web_id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=36,
                        unique=True,
                        verbose_name="product website ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="format: required, max-255",
                        max_length=255,
                        unique=True,
                        verbose_name="product name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="product description"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="is product active"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date product created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date product last updated",
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="products",
                        to="products.brand",
                    ),
                ),
                (
                    "category",
                    mptt.fields.TreeManyToManyField(
                        related_name="products", to="categories.category"
                    ),
                ),
            ],
            options={
                "verbose_name": "product",
                "verbose_name_plural": "products",
                "db_table": "products",
            },
        ),
        migrations.CreateModel(
            name="ProductAttribute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        verbose_name="product attribute name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, verbose_name="product attribute description"
                    ),
                ),
                (
                    "label",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="product_attributes",
                        to="products.label",
                    ),
                ),
            ],
            options={
                "verbose_name": "product attribute",
                "verbose_name_plural": "product attribute",
                "db_table": "product_attributes",
            },
        ),
        migrations.CreateModel(
            name="ProductAttributeValue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "value",
                    models.CharField(max_length=255, verbose_name="attribute value"),
                ),
                (
                    "product_attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="attribute_values",
                        to="products.productattribute",
                    ),
                ),
            ],
            options={
                "verbose_name": "product attribute value",
                "verbose_name_plural": "product attribute values",
                "db_table": "product_attribute_values",
            },
        ),
        migrations.CreateModel(
            name="ProductItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sku",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="stock keeping unit"
                    ),
                ),
                ("qty_in_stock", models.PositiveIntegerField(default=0)),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="format: true=product visible",
                        verbose_name="product visibility",
                    ),
                ),
                (
                    "sale_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "the price must be between 0 and 999999999.99."
                            }
                        },
                        help_text="format: maximum price 999999999.99",
                        max_digits=11,
                        verbose_name="sale price",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date sub-product created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date sub-product updated",
                    ),
                ),
            ],
            options={
                "verbose_name": "product item",
                "verbose_name_plural": "product items",
                "db_table": "product_items",
            },
        ),
        migrations.CreateModel(
            name="ProductType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="type of product"
                    ),
                ),
            ],
            options={
                "verbose_name": "product type",
                "verbose_name_plural": "product types",
                "db_table": "product_types",
            },
        ),
        migrations.CreateModel(
            name="ProductTypeAttribute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sequence", models.PositiveIntegerField()),
                (
                    "product_attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.productattribute",
                    ),
                ),
                (
                    "product_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.producttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "type and attribute",
                "verbose_name_plural": "types and attributes",
                "db_table": "product_types_attributes",
                "unique_together": {("product_attribute", "product_type")},
            },
        ),
        migrations.AddField(
            model_name="producttype",
            name="product_attributes",
            field=models.ManyToManyField(
                related_name="product_types",
                through="products.ProductTypeAttribute",
                to="products.productattribute",
            ),
        ),
        migrations.CreateModel(
            name="ProductItemAttributeValue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("to_highlight", models.BooleanField(default=False)),
                (
                    "attribute_value",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attribute_value_item_config",
                        to="products.productattributevalue",
                    ),
                ),
                (
                    "product_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item_attribute_value_config",
                        to="products.productitem",
                    ),
                ),
            ],
            options={
                "verbose_name": "product item attribute value",
                "verbose_name_plural": "product items attribute values",
                "db_table": "product_items_attribute_values",
                "unique_together": {("attribute_value", "product_item")},
            },
        ),
        migrations.AddField(
            model_name="productitem",
            name="attribute_values",
            field=models.ManyToManyField(
                related_name="product_items",
                through="products.ProductItemAttributeValue",
                to="products.productattributevalue",
            ),
        ),
        migrations.AddField(
            model_name="productitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_items",
                to="products.product",
            ),
        ),
        migrations.AddField(
            model_name="productitem",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_items",
                to="products.producttype",
            ),
        ),
        migrations.CreateModel(
            name="Media",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="images/default.png",
                        upload_to="images/product-item/",
                        verbose_name="product image",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(max_length=255, verbose_name="alternative text"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="product visibility",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date sub-product created",
                    ),
                ),
                (
                    "product_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="products.productitem",
                    ),
                ),
            ],
            options={
                "verbose_name": "product image",
                "verbose_name_plural": "product images",
                "db_table": "medias",
            },
        ),
    ]
