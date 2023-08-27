from rest_framework import serializers

from products.models import Product


class AttributesSerializer(serializers.Serializer):
    def to_representation(self, instance: Product):
        return {"attributes": instance.get_attributes_data()}