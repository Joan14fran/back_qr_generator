from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializer import CustomUserSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from django.contrib.sessions.models import Session
from django.contrib.auth import logout
from django.utils import timezone

# Create your views here.

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
  
    
class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                # Iniciar sesión y generar un token
                token, created = Token.objects.get_or_create(user=user)

                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Se requieren el nombre de usuario y la contraseña'}, status=status.HTTP_400_BAD_REQUEST)
        



