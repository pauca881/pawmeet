from django.db import models
from mascotas.models import Mascota
from django.contrib.auth.models import User  # no s'utilitza

"""
Redundancia con atributos del modelo User: Los campos como username, password, first_name y last_name ya están definidos en el modelo User de Django, por lo que no necesitas redefinirlos en UserProfile. Están disponibles a través de la relación OneToOne con el campo usuario.

Repetición innecesaria de información de mascotas: Estás definiendo fechas como fecha_nacimiento_mascota en el perfil del usuario, pero eso debería estar asociado al modelo Mascota.

Relación mal interpretada con Mascota: Si un usuario puede tener más de una mascota, lo ideal sería una relación ManyToMany en lugar de una ForeignKey.
"""
# cal crear la classe USER propia de DJANGO i tot aixo amb foreing key 1 a 1 amb aquesta classe


class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    mascota = models.ForeignKey(
        Mascota, on_delete=models.SET_NULL, null=True, blank=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento_dueño = models.DateField(blank=True, null=True)
    fecha_nacimiento_mascota = models.DateField(blank=True, null=True)
    foto_mascota = models.ImageField(upload_to='fotos/', blank=True, null=True)

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
