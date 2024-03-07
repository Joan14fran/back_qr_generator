from django.db import models
from apps.users.models import CustomUser

# Create your models here.
class QR(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    contenido = models.TextField()
    imagen_qr = models.ImageField(upload_to='qr_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.nombre}"