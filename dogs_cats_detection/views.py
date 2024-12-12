from django.shortcuts import render, redirect
from mascotas.forms import MascotaForm  
from mascotas.models import Mascota

def crear_mascota(request, mascota_id):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)  # Usamos MascotaForm para recibir tanto POST como archivos
        if form.is_valid():
            # Si el formulario es válido, guardamos la foto de la mascota
            form.save()  # Guarda el modelo Mascota, incluyendo la foto
            return redirect('perfil')  # Redirige a donde necesites (perfil, etc.)
        else:
            # Si el formulario no es válido, volvemos a renderizar la página con los errores
            return render(request, 'cargar_foto.html', {'form': form})

    else:
        form = MascotaForm()  # Si es un GET, inicializamos el formulario vacío

    return render(request, 'cargar_foto.html', {'form': form})
