from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q

from mascotas.models import Mascota, Evento
from mascotas.models import Amigos

from usuarios.models import UserProfile

from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import NearestNeighbors

import pandas as pd
import logging

# Our views
def home_view(request):
    return render(request, 'home.html')

@login_required
def conectar_view(request):
    if 'mascota_id' in request.POST:
        mascota_id = request.POST['mascota_id']
        mascota = Mascota.objects.get(id=mascota_id)
        dueño = mascota.dueño

        if dueño != request.user.userprofile:
            amistad_existente = Amigos.objects.filter(
                (Q(perfil1=request.user.userprofile) & Q(perfil2=dueño)) |
                (Q(perfil1=dueño) & Q(perfil2=request.user.userprofile))
            ).exists()

            if not amistad_existente:
                Amigos.objects.create(perfil1=request.user.userprofile, perfil2=dueño)
                mensaje = "Amistad creada con éxito"
            else:
                mensaje = "Ya son amigos o no puedes ser amigo de ti mismo"
        else:
            mensaje = "Ya son amigos o no puedes ser amigo de ti mismo"

        return render(request, 'conectar.html', {'mensaje': mensaje})

    usuario_actual = request.user
    perfil_usuario = UserProfile.objects.get(usuario=usuario_actual)
    mascotas = perfil_usuario.mascotas_datos.all()

    if not mascotas.exists():
        return render(request, 'conectar.html', {'mascotas_cercanas': [], 'usuario_actual': usuario_actual})

    primera_mascota = mascotas.first()

    df = pd.read_csv('home/dades_mascotas.csv', encoding='utf-8')
    columnas_categoricas = ['tamano', 'color', 'temperamento', 'nivel_actividad', 'nivel_socializacion', 'vacunado']
    columnas_numericas = ['peso']
    preprocesador = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(), columnas_categoricas),
            ('num', StandardScaler(), columnas_numericas)
        ])

    pipeline = Pipeline(steps=[('preprocesar', preprocesador)])
    X = pipeline.fit_transform(df)
    knn = NearestNeighbors(n_neighbors=10, metric='euclidean')
    knn.fit(X)
    nueva_mascota = pd.DataFrame({
        'tamano': [primera_mascota.tamaño],
        'color': [primera_mascota.color],
        'temperamento': [primera_mascota.temperamento],
        'nivel_actividad': [primera_mascota.nivel_actividad],
        'peso': [primera_mascota.peso],
        'nivel_socializacion': [primera_mascota.nivel_socializacion],
        'vacunado': [primera_mascota.vacunado]
    })
    X_nueva = pipeline.transform(nueva_mascota)

    distancias, indices = knn.kneighbors(X_nueva)

    ids_mascotas_cercanas = [df.iloc[idx]['id'] for idx in indices[0]]
    mascotas_cercanas = []
    for id_mascota in ids_mascotas_cercanas:
        try:
            mascota = Mascota.objects.get(pk=id_mascota)
            mascotas_cercanas.append({
                'id': mascota.id,
                'nombre': mascota.nombre,
                'raza': mascota.raza,
                'tamaño': mascota.tamaño,
                'color': mascota.color,
                'temperamento': mascota.temperamento,
                'nivel_actividad': mascota.nivel_actividad,
                'peso': mascota.peso,
                'nivel_socializacion': mascota.nivel_socializacion,
                'vacunado': mascota.vacunado,
                'distancia': distancias[0][indices[0].tolist().index(id_mascota)]
            })
        except Mascota.DoesNotExist:
            continue

    # Obtener las amistades donde el usuario es 'perfil1' o 'perfil2'
    amistades = Amigos.objects.filter(
        Q(perfil1=request.user.userprofile) | Q(perfil2=request.user.userprofile)
    )
    # Crear una lista de amigos (el perfil 1 o perfil 2 será el amigo dependiendo de cómo se haya guardado)
    amigos = []
    for amistad in amistades:
        if amistad.perfil1 != request.user.userprofile:
            amigos.append(amistad.perfil1)
        else:
            amigos.append(amistad.perfil2)
    return render(request, 'conectar.html', {'mascotas_cercanas': mascotas_cercanas, 'usuario_actual': usuario_actual, 'amigos': amigos})

def eventos_view(request):
    eventos = Evento.objects.all()

    # Pasar los eventos al contexto
    return render(request, 'meetups.html', {'eventos': eventos})

@login_required
def unirme_a_evento(request):

    evento = Evento.objects.get(id=request.GET.get('id'))
    evento.usuarios_inscritos.add(request.user.userprofile)

    return redirect('eventos')

