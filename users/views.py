from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product


# Create your views here.
def home(request):
    p = Product.objects.first()
    return render(request, template_name="users/home.html", context={"product": p})


class ProductImage(APIView):
    def get(request, *args, **kwargs):
        p = Product.objects.first()
        return Response({"product_img_url": p.product_image.url})