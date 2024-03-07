from django.shortcuts import render
from rest_framework import viewsets
from .models import QR
from .serializer import QRSerializer

# Create your views here.
class QRViewSet(viewsets.ModelViewSet):
    queryset = QR.objects.all()
    serializer_class = QRSerializer