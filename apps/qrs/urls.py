from django.urls import path, include
from rest_framework import routers
from apps.qrs import views

router = routers.DefaultRouter()
router.register(r'url-qrs', views.URLQRViewSet, basename='url-qr')
router.register(r'texto-qrs', views.TextoQRViewSet, basename='texto-qr')
router.register(r'email-qrs', views.EmailQRViewSet, basename='email-qr')
router.register(r'tarjeta-qrs', views.TarjetaPresentacionQRViewSet, basename='tarjeta-qr')

urlpatterns = [
    path('api/', include(router.urls)),
]
