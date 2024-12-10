from django.shortcuts import render
from django.http import HttpResponse
from mascotas.models import Mascota, Evento
from django.contrib.auth.decorators import login_required
from usuarios.models import UserProfile


from datetime import datetime, timedelta
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import NearestNeighbors


# Our views
def home_view(request):

    return render(request, 'home.html')


@login_required
def conectar_view(request):
    return render(request, 'conectar.html')

def eventos_view(request):
    eventos = Evento.objects.all()

    # Pasar los eventos al contexto
    return render(request, 'meetups.html', {'eventos': eventos})

def ver_mascota_cercana_view(request):
    df = pd.read_csv('home/dades_mascotas.csv', encoding='utf-8')
    columnas_categoricas = ['tamano', 'color', 'temperamento', 'nivel_actividad', 'nivel_socializacion', 'vacunado']
    #columnas_numericas = ['fecha_nacimiento','peso']
    columnas_numericas = ['peso']


    # aqui lo que hago es crear un transformador para las columnas categóricas (one-hot eencoding)
    # y para las columnas numéricas (Normalización)

    preprocesador = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(), columnas_categoricas),  #transformo las categorías en variables binarias
            ('num', StandardScaler(), columnas_numericas)    #y normAlizo las características numéricas
        ])

    # creo el pipeline que preprocesa los datos
    pipeline = Pipeline(steps=[('preprocesar', preprocesador)])

    # el pipeline lo aplico para preprocesar las características
    X = pipeline.fit_transform(df)

    # creo un modelo KNN
    # aqui lo que hago es usar NearestNeighbors para encontrar las 10 mascotas más cercanas
    knn = NearestNeighbors(n_neighbors=10, metric='euclidean')

    # ajusto el modelo con las características preprocesadas
    knn.fit(X)


    # MASCOTAS USUARIO ACTUAL
    usuario_actual = request.user
    print(f"Usuario actual: {usuario_actual.username}")

    perfil_usuario = UserProfile.objects.get(usuario=usuario_actual)
    print(f"Perfil del usuario actual: {perfil_usuario}")

    mascotas = perfil_usuario.mascotas_datos.all()
    print(f"Mascotas del usuario actual: {mascotas}")

    primera_mascota = mascotas.first()
    print(f"Primera mascota del usuario actual: {primera_mascota}")

    nueva_mascota = pd.DataFrame({
        #'fecha_nacimiento': [datetime.now() - timedelta(days=3*365)], 
        'tamano': ['Mediano'],
        'color': ['Blanco'],
        'temperamento': ['Tranquilo'],
        'nivel_actividad': ['Alto'],
        'peso': [50], 
        'nivel_socializacion': ['Alta'],  
        'vacunado': [True] 
    })


    # transformo la nueva mascota con el mismo pipeline
    X_nueva = pipeline.transform(nueva_mascota)

    # aqui enceuntro la mascota más cercana
    distancias, indices = knn.kneighbors(X_nueva)

    # Mostrar el ID de la mascota más cercana
    # mascota_mas_cercana = df.iloc[indices[0][0]]
    # print(f'La mascota más cercana es: {mascota_mas_cercana["id"]}')

    # Obtener los ids de las mascotas más cercanas
    ids_mascotas_cercanas = [df.iloc[idx]['id'] for idx in indices[0]]

    # Consultar la base de datos para obtener detalles completos de las mascotas más cercanas
    mascotas_cercanas = []
    for id_mascota in ids_mascotas_cercanas:
        try:
            # Buscar la mascota por su id en la base de datos
            mascota = Mascota.objects.get(pk=id_mascota)
            print(mascota)
            mascotas_cercanas.append({
                'id': mascota.id,

                'nombre': mascota.nombre,

                'tamaño': mascota.tamaño,
                'color': mascota.color,
                'temperamento': mascota.temperamento,
                'nivel_actividad': mascota.nivel_actividad,
                'peso': mascota.peso,
                'nivel_socializacion': mascota.nivel_socializacion,
                'vacunado': mascota.vacunado,
                'distancia': distancias[0][indices[0].tolist().index(id_mascota)]  # Relacionar la distancia con el id
            })
            
        except Mascota.DoesNotExist:
            print(f"Error: No se encontró la mascota con id {id_mascota}")
            # En lugar de hacer un raise, podrías agregar la mascota con un mensaje de error o dejarla fuera
            mascotas_cercanas.append({
                'id': id_mascota,
                'error': 'Mascota no encontrada'
            })


    # Pasar los datos al contexto para el renderizado
    context = {
        'mascotas_cercanas': mascotas_cercanas
    }

    print(mascotas_cercanas)

    return render(request, 'mostrar_mascota_cercana.html', {**context, 'usuario_actual': usuario_actual})



# View sencilla para listar mascotas
def list_mascotas_view(request):
    mascotas = Mascota.objects.all()
    context = {
        'mascotas': mascotas
    }

    return render(request, 'list_mascotas.html', context)



