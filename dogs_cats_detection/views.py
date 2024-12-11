<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
# ESQUEMATICAMENT ES FA AIXI, PERO NO ENTENC (I COM TAMPOC TENIM USUARIS CREATS) COM FER ARRIBER LES IMATGES FINS A PATH, ENTENC QUE
# SERA VIA UN FORMULARI, PER AIXO ESTA FET AMB AQUEST OBJECTIU

# HO DEIXO TOT COMENTAT PER AQUEST MOTIU, SI ALGU EM POT DONAR UN COP D'ULL A VEURE SI VEU COM

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from dogs_cats_detection.tl_models import predict

def subir_foto_mascota(request):
    if request.method == 'POST' and request.FILES['foto']:
        foto_subida = request.FILES['foto']
        fs = FileSystemStorage()
        ruta_imagen = fs.save(foto_subida.name, foto_subida)
        ruta_completa = fs.url(ruta_imagen)
        resultado = predict(ruta_completa)

        return render(request, 'resultado.html', {'resultado': resultado, 'ruta_imagen': ruta_completa})
    return render(request, 'subir_foto.html')

a = 2
>>>>>>> main
