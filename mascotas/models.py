import os
import json
from django.db import models

# Función para cargar las opciones de razas desde el archivo JSON
def load_razas_opciones():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    razas_path = os.path.join(current_dir, 'razas.json')
    with open(razas_path, 'r', encoding='utf-8') as f:
        return json.load(f)

class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='mascotas/', blank=True, null=True)
    dueño = models.ForeignKey('usuarios.UserProfile', on_delete=models.CASCADE, related_name="mascotas_datos")

    # Campos para el algoritmo KNN
    raza = models.CharField(
        max_length=50,
        choices=load_razas_opciones(),
        blank=False,
        null=False,
    )
    tamaño = models.CharField(
        max_length=50,
        choices=[('Pequeño', 'Pequeño'), ('Mediano', 'Mediano'), ('Grande', 'Grande')],
        blank=True,
        null=True
    )
    color = models.CharField(
        max_length=50,
        choices=[
            ('Negro', 'Negro'), ('Blanco', 'Blanco'), ('Gris', 'Gris'), ('Marrón', 'Marrón'),
            ('Amarillo', 'Amarillo'), ('Naranja', 'Naranja'), ('Beige', 'Beige'), ('Rojo', 'Rojo'),
            ('Azul', 'Azul'), ('Verde', 'Verde'), ('Pardo', 'Pardo'), ('Dorado', 'Dorado'),
            ('Plata', 'Plata'), ('Morado', 'Morado'), ('Rosado', 'Rosado'), ('Café', 'Café'),
            ('Celeste', 'Celeste'), ('Blanco y negro', 'Blanco y negro'), ('Tricolor', 'Tricolor'),
            ('Atigrado', 'Atigrado')
        ],
        blank=True,
        null=True
    )
    temperamento = models.CharField(
        max_length=50,
        choices=[
            ('Activo', 'Activo'), ('Juguetón', 'Juguetón'), ('Tranquilo', 'Tranquilo'), ('Independiente', 'Independiente'),
            ('Sociable', 'Sociable'), ('Cariñoso', 'Cariñoso'), ('Protector', 'Protector'), ('Cauteloso', 'Cauteloso'),
            ('Tímido', 'Tímido'), ('Agresivo', 'Agresivo'), ('Dominante', 'Dominante'), ('Curioso', 'Curioso'),
            ('Desobediente', 'Desobediente'), ('Obediente', 'Obediente'), ('Amigable', 'Amigable')
        ],
        blank=True,
        null=True
    )
    nivel_actividad = models.CharField(
        max_length=50,
        choices=[('Bajo', 'Bajo'), ('Medio', 'Medio'), ('Alto', 'Alto')],
        blank=True,
        null=True
    )
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nivel_socializacion = models.CharField(
        max_length=50,
        choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')],
        blank=True,
        null=True
    )
    vacunado = models.BooleanField(default=False)

    # Agregar el campo 'castrado'
    castrado = models.BooleanField(default=False)  # Este campo indica si la mascota está castrada

    def __str__(self):
        return (
            f"ID: {self.id} - Nombre: {self.nombre} - Fecha de nacimiento: {self.fecha_nacimiento} - "
            f"Foto: {self.foto} - Dueño: {self.dueño} - Raza: {self.raza} - Tamaño: {self.tamaño} - "
            f"Color: {self.color} - Temperamento: {self.temperamento} - Nivel de actividad: {self.nivel_actividad} - "
            f"Peso: {self.peso} - Nivel de socialización: {self.nivel_socializacion} - Vacunado: {self.vacunado} - "
            f"Castrado: {self.castrado}"
        )

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
    usuarios_inscritos = models.ManyToManyField(
        'usuarios.UserProfile', related_name='eventos_inscritos', blank=True
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
