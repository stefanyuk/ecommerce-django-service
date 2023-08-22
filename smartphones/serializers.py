from rest_framework import serializers


from smartphones.models import Smartphone

MIN_QTY_IN_STOCK = 0


class SmartphoneSerializer(serializers.ModelSerializer):
    sku = serializers.CharField(source="product.sku")
    is_available = serializers.SerializerMethodField()
    price = serializers.DecimalField(source="product.price")
    color = serializers.CharField(source="product.color.name")
    brand = serializers.CharField(source="product.brand.name")   

    class Meta:
        db_model = Smartphone
        fields = [
            "display_name"
        ]
    
    def get_is_available(self, smartphone: Smartphone):
        return smartphone.product.qty_in_stock > MIN_QTY_IN_STOCK