from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializer import CustomUserSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.hashers import make_password

# Create your views here.

class CustomUserViewSet(viewsets.ModelViewSet, ObtainAuthToken):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
  
    

class LoginAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # Verificar que se proporcionaron ambos campos
        if not username or not password:
            return Response({'error': 'Se requieren el nombre de usuario y la contraseña'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        # Verificar si la autenticación fue exitosa
        if user:
            # Iniciar sesión manualmente para actualizar last_login
            login(request, user)

            # Generar un token si no existe, o recuperar el existente
            token, created = Token.objects.get_or_create(user=user)

            # Serializar los datos del usuario utilizando tu serializador personalizado
            user_data = CustomUserSerializer(user).data

            # Devolver solo el token y el ID del usuario
            response_data = {
                'token': token.key,
                'user_id': user_data['id']
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # Devolver un error si las credenciales son inválidas
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Invalidar el token de autenticación del usuario actual
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        except AttributeError:
            # Usuario no autenticado
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class ChangePasswordAPIView(APIView):
    def post(self, request):
        # Obtener el usuario actualmente autenticado
        user = request.user

        # Verificar si el usuario proporcionó la contraseña actual y la nueva contraseña
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        if not current_password or not new_password:
            return Response({'error': 'Se requiere la contraseña actual y la nueva contraseña'}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar si la contraseña actual es válida
        if not user.check_password(current_password):
            return Response({'error': 'La contraseña actual no es válida'}, status=status.HTTP_400_BAD_REQUEST)

        # Cambiar la contraseña del usuario
        user.set_password(new_password)
        user.save()

        return Response({'message': 'Contraseña cambiada exitosamente'}, status=status.HTTP_200_OK)




