from django.urls import path, include
from rest_framework import routers
from apps.qrs import views

router = routers.DefaultRouter()
router.register(r'qrs', views.QRViewSet, basename='qr')

urlpatterns = [
    path("api/", include(router.urls)),
]
