from django.contrib import admin

from .models import Smartphone, CameraFeatures, CommunicationStandarts


admin.site.register(Smartphone)
admin.site.register(CameraFeatures)
admin.site.register(CommunicationStandarts)
