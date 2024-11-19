# Generated by Django 5.1.3 on 2024-11-19 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mascotas', '0001_initial'),
        ('usuarios', '0002_profesionaluser_reseña_tipoprofesional_userprofile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigos',
            name='perfil1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amigos_de', to='usuarios.userprofile'),
        ),
        migrations.AddField(
            model_name='amigos',
            name='perfil2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amigos_con', to='usuarios.userprofile'),
        ),
        migrations.AddField(
            model_name='evento',
            name='organizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='usuarios.userprofile'),
        ),
        migrations.AddField(
            model_name='mascota',
            name='dueño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mascotas', to='usuarios.userprofile'),
        ),
        migrations.AddField(
            model_name='mascota',
            name='tipo_mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mascotas.tipomascota'),
        ),
        migrations.AlterUniqueTogether(
            name='amigos',
            unique_together={('perfil1', 'perfil2')},
        ),
    ]
