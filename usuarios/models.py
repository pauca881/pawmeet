from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(max_length=100, blank=True, null=True)
    fecha_nacimiento_dueño = models.DateField(blank=True, null=True)
    mascotas = models.ManyToManyField('mascotas.Mascota', blank=True, related_name="usuarios_perfiles")
    User._meta.get_field('email')._unique = False

    def __str__(self):
        return self.usuario.username

class TipoProfesional(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class ProfesionalUser(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profesional_profile')
    nombre_establecimiento = models.CharField(max_length=150)
    tipo_de_profesional = models.OneToOneField(TipoProfesional, on_delete=models.CASCADE)
    direccion = models.TextField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    foto_establecimiento = models.ImageField(upload_to='establecimientos/', blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.nombre_establecimiento}"

class Reseña(models.Model):
    id = models.AutoField(primary_key=True)
    profesional = models.ForeignKey(ProfesionalUser, on_delete=models.CASCADE, related_name='reseñas')
    numero_estrellas = models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reseña: {self.titulo} ({self.numero_estrellas} estrellas)"
