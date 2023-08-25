from rest_framework.views import APIView
from rest_framework.request import Request
from .models import ProductItem
from .serializers import ProductItemDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict


def get_product_item(product_item_id: int) -> ProductItem:
    try:
        return ProductItem.objects\
        .prefetch_related("attribute_values__product_attribute")\
        .select_related("product")\
        .get(id=product_item_id)
    except ProductItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class ProductItemDetail(APIView):
    def get(self, request: Request, product_id: int):
        product_item = get_product_item(product_id)
        serializer = ProductItemDetailSerializer(product_item)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductItemVariations(APIView):
    def get(self, request: Request, product_id: int):
        product_item = get_product_item(product_id)
        target_item_color_attribute = product_item.color
        sibling_product_items = ProductItem.objects.get_sibling_product_items(product_item)

        attributes = defaultdict(list)

        if target_item_color_attribute is not None:
            for item in sibling_product_items:
                if item.color == target_item_color_attribute:
                    item_non_common_attributes = item.get_non_common_attributes().exclude(product_attribute__name="Color")
                    for attr in item_non_common_attributes:
                        attributes[attr.product_attribute.name].append(
                            {
                                "value": attr.value,
                                "qty_in_stock": item.qty_in_stock,
                                "product_item_id": item.id
                            }
                        )

        return Response(data=attributes, status=200)


class ProductItemAttributes(APIView):
    def get(self, request: Request, product_id: int):
        pass