from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Campo de contraseña solo para escritura

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'nombre', 'apellido', 'password']

    def create(self, validated_data):
        # Hashea la contraseña antes de guardarla en la base de datos
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
