# Generated by Django 5.1.3 on 2024-11-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0002_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoMascota',
        ),
        migrations.AddField(
            model_name='mascota',
            name='color',
            field=models.CharField(blank=True, choices=[('Negro', 'Negro'), ('Blanco', 'Blanco'), ('Gris', 'Gris'), ('Marrón', 'Marrón'), ('Amarillo', 'Amarillo'), ('Naranja', 'Naranja'), ('Beige', 'Beige'), ('Rojo', 'Rojo'), ('Azul', 'Azul'), ('Verde', 'Verde'), ('Pardo', 'Pardo'), ('Dorado', 'Dorado'), ('Plata', 'Plata'), ('Morado', 'Morado'), ('Rosado', 'Rosado'), ('Café', 'Café'), ('Celeste', 'Celeste'), ('Blanco y negro', 'Blanco y negro'), ('Tricolor', 'Tricolor'), ('Atigrado', 'Atigrado')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='nivel_actividad',
            field=models.CharField(blank=True, choices=[('Bajo', 'Bajo'), ('Medio', 'Medio'), ('Alto', 'Alto')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='nivel_socializacion',
            field=models.CharField(blank=True, choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='tamaño',
            field=models.CharField(blank=True, choices=[('Pequeño', 'Pequeño'), ('Mediano', 'Mediano'), ('Grande', 'Grande')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='temperamento',
            field=models.CharField(blank=True, choices=[('Activo', 'Activo'), ('Juguetón', 'Juguetón'), ('Tranquilo', 'Tranquilo'), ('Independiente', 'Independiente'), ('Sociable', 'Sociable'), ('Cariñoso', 'Cariñoso'), ('Protector', 'Protector'), ('Cauteloso', 'Cauteloso'), ('Tímido', 'Tímido'), ('Agresivo', 'Agresivo'), ('Dominante', 'Dominante'), ('Curioso', 'Curioso'), ('Desobediente', 'Desobediente'), ('Obediente', 'Obediente'), ('Amigable', 'Amigable')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='vacunado',
            field=models.BooleanField(default=False),
        ),
    ]