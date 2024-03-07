from rest_framework import viewsets
from .models import CustomUser
from .serializer import CustomUserSerializer

# Create your views here.
class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
