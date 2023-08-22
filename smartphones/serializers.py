from rest_framework import serializers
from smartphones.models import Smartphone

MIN_QTY_IN_STOCK = 0


class SmartphoneSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="product.web_id")
    sku = serializers.CharField(source="product.sku")
    is_available = serializers.SerializerMethodField()
    price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2)
    color = serializers.CharField(source="product.color.name")
    brand = serializers.CharField(source="product.brand.name")
    attributes_data = serializers.SerializerMethodField()

    class Meta:
        model = Smartphone
        fields = [
            "id",
            "sku",
            "price",
            "color",
            "brand",
            "attributes_data",
            "is_available",
            "display_name",
        ]
    
    def get_is_available(self, smartphone: Smartphone) -> bool:
        return smartphone.product.qty_in_stock > MIN_QTY_IN_STOCK

    def get_attributes_data(self, obj: Smartphone) -> dict:
        return obj.get_attributes_data()