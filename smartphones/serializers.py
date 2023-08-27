from rest_framework import serializers
from smartphones.models import Smartphone


class SmartphoneSerializer(serializers.ModelSerializer):
    color = serializers.CharField(source="color.name")
    brand = serializers.CharField(source="brand.name")
    variations = serializers.SerializerMethodField()

    class Meta:
        model = Smartphone
        fields = [
            "id",
            "sku",
            "sale_price",
            "color",
            "brand",
            "display_name",
            "is_available",
            "variations",
        ]
        read_only_fields = ["id", "display_name", "is_available", "variations"]

    def get_variations(self, obj: Smartphone) -> dict:
        variations = [
            self._prepare_color_variations(obj),
            self._prepare_internal_memory_variations(obj)
        ]
        return variations

    def _prepare_color_variations(self, obj: Smartphone) -> dict:
        color_variations = Smartphone.objects.get_color_variations_by_internal_memory(obj)
        color_variations_data = {"title": "Color", "options": [], "is_color": True}

        for variation in color_variations:
            color_variations_data["options"].append(
                {
                    "label": variation.color.name,
                    "hex": variation.color.hex,
                    "is_current": variation.color == obj.color,
                    "is_available": variation.is_available(),
                    "url": variation.get_absolute_url()
                }
            )

        return color_variations_data

    def _prepare_internal_memory_variations(self, obj: Smartphone) -> dict:
        internal_memory_variations = Smartphone.objects.get_internal_memory_variations_by_color(obj)
        internal_memory_variations_data = {"title": "Internal Memory", "options": [], "is_color": False}

        for variation in internal_memory_variations:
            internal_memory_variations_data["options"].append(
                {
                    "label": variation.internal_memory,
                    "is_current": variation.internal_memory == obj.internal_memory,
                    "is_available": variation.is_available(),
                    "url": variation.get_absolute_url()
                }
            )

        return internal_memory_variations_data
