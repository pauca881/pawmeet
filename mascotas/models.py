from django.db import models

class TipoMascota(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='mascotas/', blank=True, null=True)
    dueño = models.ForeignKey('usuarios.UserProfile', on_delete=models.CASCADE, related_name="mascotas_datos")
    tipo = models.ForeignKey(TipoMascota, on_delete=models.CASCADE, related_name="mascotas")


    def __str__(self):
        return f"{self.nombre} - {self.tipo.nombre}"


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