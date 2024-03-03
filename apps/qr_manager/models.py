from django.db import models
from apps.users.models import CustomUser
# Create your models here.
class QR(models.Model):
    ID_QR = models.AutoField(primary_key=True)
    Contenido = models.TextField()
    Estilos = models.CharField(max_length=255)  # Puedes ajustar esto según tus necesidades
    Usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"QR {self.ID_QR}: {self.Contenido}"