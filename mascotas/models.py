from django.db import models

from django.db import models

class TipoMascota(models.Model):
    """
    Representa el tipo de mascota (ejemplo: perro, gato, ave).
    Este modelo solo puede ser modificado desde el admin.
    """
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    """
    Representa una mascota vinculada a un perfil de usuario.
    """
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()  # Edad en años
    tipo_mascota = models.ForeignKey(TipoMascota, on_delete=models.PROTECT)
    dueño = models.ForeignKey(
        'usuarios.UserProfile', on_delete=models.CASCADE, related_name='mascotas'
    )

    def __str__(self):
        return f"{self.nombre} ({self.tipo_mascota.nombre})"


class Evento(models.Model):
    """
    Representa eventos relacionados con mascotas, creados por usuarios.
    """
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField()
    ubicacion = models.CharField(max_length=255)
    organizador = models.ForeignKey(
        'usuarios.UserProfile', on_delete=models.CASCADE, related_name='eventos'
    )

    def __str__(self):
        return self.titulo


class Amigos(models.Model):
    """
    Representa una relación de amistad entre perfiles de usuarios.
    """
    perfil1 = models.ForeignKey(
        'usuarios.UserProfile', on_delete=models.CASCADE, related_name='amigos_de'
    )
    perfil2 = models.ForeignKey(
        'usuarios.UserProfile', on_delete=models.CASCADE, related_name='amigos_con'
    )
    fecha_conexion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('perfil1', 'perfil2')  # Evita duplicados

    def __str__(self):
        return f"Amistad entre {self.perfil1} y {self.perfil2}"