from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'nombre', 'apellido', 'password', 'is_staff', 'is_active', 'fecha_nacimiento', 'numero_celular', 'genero']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))
        else:
            validated_data.pop('password', None)
        return super().update(instance, validated_data)
