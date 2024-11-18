from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.TextField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen_perfil = models.ImageField(
        upload_to='perfiles/', blank=True, null=True)

    def __str__(self):
        return self.nombre
