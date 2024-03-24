from rest_framework import serializers
from .models import URLQR, TextoQR, EmailQR, TarjetaPresentacionQR, BaseQR

class BaseQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseQR
        fields = ['id', 'user', 'nombre', 'tamaño', 'redundancia', 'imagen_qr']

class URLQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLQR
        fields = '__all__'

class TextoQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextoQR
        fields = '__all__'

class EmailQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailQR
        fields = '__all__'

class TarjetaPresentacionQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjetaPresentacionQR
        fields = '__all__'
