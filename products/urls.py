from django.urls import path
from . import views


urlpatterns = [
    path("<int:product_id>/", views.ProductItemDetail.as_view(), name="product-item-detail"),
    path("<int:product_id>/variations", views.ProductItemVariations.as_view(), name="product-item-variations"),
    path("<int:product_id>/attributes", views.ProductItemAttributes.as_view(), name="product-item-attributes"),
]