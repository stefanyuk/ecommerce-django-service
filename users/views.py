from django.shortcuts import render

from .models import Product


# Create your views here.
def home(request):
    p = Product.objects.first()
    return render(request, template_name="users/home.html", context={"product": p})