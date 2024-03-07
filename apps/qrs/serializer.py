from rest_framework import serializers
from .models import QR

class QRSerializer(serializers.ModelSerializer):
    class Meta:
        model = QR
        fields = '__all__'