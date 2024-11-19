from django.db import models
from mascotas.models import Mascota, TipoMascota
from django.contrib.auth.models import User


class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    mascota = models.ForeignKey(
        Mascota, on_delete=models.SET_NULL, null=True, blank=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(max_length=100, blank=True, null=True)
    fecha_nacimiento_dueño = models.DateField(blank=True, null=True)
    fecha_nacimiento_mascota = models.DateField(blank=True, null=True)
    foto_persona = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def __str__(self):
        return self.usuario.username


class TipoProfesional(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class ProfesionalUser(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profesional_profile')
    nombre_establecimiento = models.CharField(max_length=150)
    tipo_de_profesional = models.OneToOneField(
        TipoProfesional, on_delete=models.CASCADE)
    direccion = models.TextField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    foto_establecimiento = models.ImageField(
        upload_to='establecimientos/', blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.nombre_establecimiento}"


class Reseña(models.Model):
    id = models.AutoField(primary_key=True)
    profesional = models.ForeignKey(
        ProfesionalUser, on_delete=models.CASCADE, related_name='reseñas')
    numero_estrellas = models.PositiveSmallIntegerField(default=0)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reseña: {self.titulo} ({self.numero_estrellas} estrellas)"


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
