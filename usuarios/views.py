from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from usuarios.models import UserProfile
from usuarios.forms import UserProfileCreationForm, UserForm
from mascotas.forms import MascotaForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import csv
from django.conf import settings
from mascotas.models import Mascota


def listar_usuarios(request):
    usuarios = User.objects.all()  # Usuarios registrados
    perfiles = UserProfile.objects.all()  # Perfiles de usuario
    return render(request, 'listar_usuarios.html', {
        'usuarios': usuarios,
        'perfiles': perfiles
    })

def crear_usuario(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileCreationForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # Guardar el usuario
            usuario = user_form.save(commit=False)
            usuario.set_password(user_form.cleaned_data['password'])
            usuario.save()

            # Guardar el perfil asociado al usuario
            perfil = profile_form.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

            # Agregar un mensaje de éxito
            messages.success(request, 'Usuario creado exitosamente.')

            # Redirigir a la página de crear mascota
            return redirect('crear_mascota', usuario_id=usuario.id)

    else:
        user_form = UserForm()
        profile_form = UserProfileCreationForm()

    return render(request, 'crear_usuario.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def crear_mascota(request, usuario_id):
    perfil = get_object_or_404(UserProfile, usuario_id=usuario_id)

    if request.method == 'POST':
        mascota_form = MascotaForm(request.POST, request.FILES)
        if mascota_form.is_valid():
            mascota = mascota_form.save(commit=False)
            mascota.dueño = perfil  # Relacionar con el perfil del usuario
            mascota.save()

            #  # Datos de la mascota a guardar en el archivo CSV
            # mascota_data = [
            #     mascota.id,
            #     mascota.fecha_nacimiento,
            #     mascota.tamaño,
            #     mascota.color,
            #     mascota.temperamento,
            #     mascota.nivel_actividad,
            #     mascota.peso,
            #     mascota.nivel_socializacion,
            #     mascota.vacunado,
            #     mascota.dueño.usuario_id  # Guardamos el ID del dueño
            # ]

            # file_path = r'/home/dades_mascotas.csv'

            # # Abrir el archivo CSV en modo append y escribir los datos
            # with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            #     writer = csv.writer(file)
            #     # Si el archivo está vacío, agregar encabezado
            #     if file.tell() == 0:
            #         writer.writerow([
            #             'ID', 'Fecha Nacimiento', 'Tamaño', 'Color', 'Temperamento', 
            #             'Nivel Actividad', 'Peso', 'Nivel Socialización', 'Vacunado', 'Dueño ID'
            #         ])
            #     writer.writerow(mascota_data)

            # Agregar un mensaje de éxito
            messages.success(request, 'Mascota añadida.')

            # Renderizar la misma plantilla con el mensaje
            return render(request, 'crear_mascota.html', {
                'mascota_form': mascota_form,
                'messages': messages.get_messages(request)  # Pasar los mensajes
            })
    else:
        mascota_form = MascotaForm()

    return render(request, 'crear_mascota.html', {'mascota_form': mascota_form})

def usuario_exitoso(request):
    return render(request, 'usuario_exitoso.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"¡Bienvenido, {username}!")
                return redirect('conectar')  # Redirige a la vista conectar
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('login')  # Redirige a la página de login después del logout

@login_required
def perfil(request):
    return render(request, 'perfil.html')
