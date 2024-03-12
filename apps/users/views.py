from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializer import CustomUserSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken

# Create your views here.

class CustomUserViewSet(viewsets.ModelViewSet, ObtainAuthToken):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
  
    
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token

class LoginAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user:
                # Iniciar sesión manualmente para actualizar last_login
                login(request, user)

                # Generar un token
                token, created = Token.objects.get_or_create(user=user)

                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Se requieren el nombre de usuario y la contraseña'}, status=status.HTTP_400_BAD_REQUEST)

      
        
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Invalidar el token de autenticación del usuario actual
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        except AttributeError:
            # Usuario no autenticado
            return Response(status=status.HTTP_200_OK)

