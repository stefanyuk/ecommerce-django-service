from rest_framework import serializers
from .models import ProductItem, ProductAttributeValue


class ProductItemHighlightedAttributeSerializer(serializers.Serializer):
    label = serializers.CharField()
    value = serializers.CharField()
    icon_url = serializers.CharField()


class ProductItemAttributeSerializer(serializers.Serializer):
    pass


class ProductItemDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="product.name")
    highlighted_attributes = ProductItemHighlightedAttributeSerializer(many=True)
    variations = serializers.SerializerMethodField()

    class Meta:
        model = ProductItem
        fields = [
            "name",
            "highlighted_attributes",
            "sale_price",
            "available_filter_keys"
        ]
