from django.urls import path

from smartphones import views


urlpatterns = [
    path("<int:smartphone_id>/", views.SmartphoneDetail.as_view(), name="smartphone-detail"),
    path("<int:smartphone_id>/attributes", views.SmartphoneAttributes.as_view(), name="smartphone-attributes"),
]