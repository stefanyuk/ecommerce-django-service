from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response



class SmartphoneDetail(APIView):
    def get(self, request: Request, smartphone_id: int) -> Response:
        pass