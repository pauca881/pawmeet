# Generated by Django 5.1.3 on 2024-12-13 16:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mascotas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProfesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfesionalUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_establecimiento', models.CharField(max_length=150)),
                ('direccion', models.TextField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('foto_establecimiento', models.ImageField(blank=True, null=True, upload_to='establecimientos/')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profesional_profile', to=settings.AUTH_USER_MODEL)),
                ('tipo_de_profesional', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.tipoprofesional')),
            ],
        ),
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_estrellas', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reseñas', to='usuarios.profesionaluser')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.TextField(blank=True, max_length=100, null=True)),
                ('fecha_nacimiento_dueño', models.DateField(blank=True, null=True)),
                ('mascotas', models.ManyToManyField(blank=True, related_name='usuarios_perfiles', to='mascotas.mascota')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
