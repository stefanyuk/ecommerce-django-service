# Generated by Django 4.2.4 on 2023-08-25 12:28

from django.db import migrations, models
import django.db.models.deletion
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
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "brand",
                "verbose_name_plural": "brands",
                "db_table": "brands",
            },
        ),
        migrations.CreateModel(
            name="Color",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("hex", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "color",
                "verbose_name_plural": "colors",
                "db_table": "colors",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "web_id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=255,
                        verbose_name="web display id",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "sku",
                    models.CharField(
                        max_length=250, unique=True, verbose_name="stock keeping unit"
                    ),
                ),
                (
                    "sale_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="selling price"
                    ),
                ),
                (
                    "stock_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="stock price"
                    ),
                ),
                (
                    "qty_in_stock",
                    models.PositiveIntegerField(
                        default=0, verbose_name="available quantity"
                    ),
                ),
                ("released_on", models.DateField(verbose_name="release year")),
                ("warranty_period_in_months", models.PositiveIntegerField()),
                (
                    "weight",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="weight"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "brand",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="products.brand",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="categories.category",
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="products.color",
                        verbose_name="color",
                    ),
                ),
            ],
            options={
                "verbose_name": "product",
                "verbose_name_plural": "products",
                "db_table": "products",
            },
        ),
    ]
