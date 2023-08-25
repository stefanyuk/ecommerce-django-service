from rest_framework import serializers
from .models import ProductItem, COLOR_ATTRIBUTE_NAME
from django.db.models.query import QuerySet


class ProductItemHighlightedAttributeSerializer(serializers.Serializer):
    label = serializers.CharField()
    value = serializers.CharField()
    icon_url = serializers.CharField()


class ProductItemAttributeSerializer(serializers.Serializer):
    pass


class ProductItemDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="product.name")
    highlighted_attributes = ProductItemHighlightedAttributeSerializer(many=True)

    class Meta:
        model = ProductItem
        fields = [
            "name",
            "highlighted_attributes",
            "sale_price"
        ]


class ProductItemVariations(serializers.BaseSerializer):
    def to_representation(self, product_item: ProductItem):
        target_item_color_attribute = product_item.color
        sibling_product_items = ProductItem.objects.get_sibling_product_items(product_item)
        variations_data = {}

        if target_item_color_attribute is not None:
            color_variations = self._prepare_item_color_variations(product_item)

    def _prepare_item_color_variations(self, product_item: ProductItem, sibling_items: QuerySet[ProductItem]) -> dict:
        pass