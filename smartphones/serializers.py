from rest_framework import serializers
from smartphones.models import Smartphone


class SmartphoneSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="web_id")
    color = serializers.CharField(source="color.name")
    brand = serializers.CharField(source="brand.name")
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

    def get_attributes_data(self, obj: Smartphone) -> dict:
        return obj.get_attributes_data()