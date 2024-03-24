from django.db import models
from apps.users.models import CustomUser

# Create your models here.
class BaseQR(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    tamaño = models.CharField(max_length=50)
    redundancia = models.CharField(max_length=50)
    imagen_qr = models.ImageField(upload_to='qr_images/', blank=True, null=True)

    class Meta:
        abstract = True

class URLQR(BaseQR):
    contenido = models.URLField()

class TextoQR(BaseQR):
    contenido = models.TextField()

class EmailQR(BaseQR):
    contenido = models.EmailField()

class TarjetaPresentacionQR(BaseQR):
    nombre_apellido = models.CharField(max_length=255)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    web = models.URLField()
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - Tarjeta de Presentación - {self.nombre}"
