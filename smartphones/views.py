from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from smartphones.models import Smartphone
from smartphones.serializers import SmartphoneSerializer
from products.serializers import AttributesSerializer


class SmartphoneApiBaseView(APIView):
    def get_object(self, smartphone_id: int) -> Smartphone:
        try:
            return Smartphone.objects\
                .select_related("product")\
                .select_related("color")\
                .select_related("brand")\
                .select_related("category")\
                .prefetch_related("main_camera_features")\
                .prefetch_related("front_camera_features")\
                .get(id=smartphone_id) #TODO: change to web_id
        except Smartphone.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SmartphoneDetail(SmartphoneApiBaseView):
    def get(self, request: Request, smartphone_id: int) -> Response:
        smartphone = self.get_object(smartphone_id)
        serializer = SmartphoneSerializer(smartphone)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SmartphoneAttributes(SmartphoneApiBaseView):
    def get(self, request: Request, smartphone_id: int) -> Response:
        smartphone = self.get_object(smartphone_id)
        serializer = AttributesSerializer(smartphone)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
