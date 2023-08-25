from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from smartphones.models import Smartphone
from smartphones.serializers import SmartphoneSerializer


class SmartphoneDetail(APIView):
    def get(self, request: Request, smartphone_id: int) -> Response:
        try:
            smartphone = Smartphone.objects\
                .select_related("product")\
                .select_related("color")\
                .select_related("brand")\
                .select_related("category")\
                .get(id=smartphone_id)
        except Smartphone.DoesNotExist:
            return Response(status=400)

        serializer = SmartphoneSerializer(smartphone)

        return Response(data=serializer.data, status=200)
        
        