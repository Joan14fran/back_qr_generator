from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # Agregar campos adicionales
    nombre = models.CharField(max_length=30, blank=True)
    apellido = models.CharField(max_length=30, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    numero_celular = models.CharField(max_length=15, blank=True, null=True)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], blank=True, null=True)

    def __str__(self):
        return self.username