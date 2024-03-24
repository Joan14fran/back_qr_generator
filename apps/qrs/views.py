from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import URLQR, TextoQR, EmailQR, TarjetaPresentacionQR
from .serializer import URLQRSerializer, TextoQRSerializer, EmailQRSerializer, TarjetaPresentacionQRSerializer

class URLQRViewSet(viewsets.ModelViewSet):
    queryset = URLQR.objects.all()
    serializer_class = URLQRSerializer
    permission_classes = [IsAuthenticated]

class TextoQRViewSet(viewsets.ModelViewSet):
    queryset = TextoQR.objects.all()
    serializer_class = TextoQRSerializer
    permission_classes = [IsAuthenticated]

class EmailQRViewSet(viewsets.ModelViewSet):
    queryset = EmailQR.objects.all()
    serializer_class = EmailQRSerializer
    permission_classes = [IsAuthenticated]

class TarjetaPresentacionQRViewSet(viewsets.ModelViewSet):
    queryset = TarjetaPresentacionQR.objects.all()
    serializer_class = TarjetaPresentacionQRSerializer
    permission_classes = [IsAuthenticated]
