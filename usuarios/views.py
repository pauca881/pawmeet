from django.shortcuts import render, redirect, get_object_or_404
from usuarios.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from usuarios.forms import UserProfileCreationForm, UserForm
from mascotas.forms import MascotaForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def listar_usuarios(request):
    usuarios = User.objects.all()  # Usuarios registrados
    perfiles = UserProfile.objects.all()  # Perfiles de usuario
    return render(request, 'listar_usuarios.html', {
        'usuarios': usuarios,
        'perfiles': perfiles
    })

def crear_usuario(request):
    if request.method == 'POST':
        print("Formulario enviado")
        user_form = UserForm(request.POST)
        profile_form = UserProfileCreationForm(request.POST, request.FILES)
        mascota_form = MascotaForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid() and mascota_form.is_valid():
            # Guardar el usuario
            usuario = user_form.save(commit=False)
            usuario.set_password(user_form.cleaned_data['password'])
            usuario.save()

            # Guardar el perfil asociado al usuario
            perfil = profile_form.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

            # Guardar la mascota asociada al usuario
            mascota = mascota_form.save(commit=False)
            mascota.dueño = perfil  # Relacionar con el perfil del usuario
            mascota.save()

            messages.success(request, "Usuario y mascota creados exitosamente.")
            return redirect('usuario_exitoso')  # Redirigir a la vista de éxito
    else:
        user_form = UserForm()
        profile_form = UserProfileCreationForm()
        mascota_form = MascotaForm()

    return render(request, 'user_profile_form.html', {
        'user_form': user_form,
        'user_profile_form': profile_form,
        'mascota_form': mascota_form,
    })

def crear_mascota(request, usuario_id):
    perfil = get_object_or_404(UserProfile, profile_id=usuario_id)

    if request.method == 'POST':
        mascota_form = MascotaForm(request.POST, request.FILES)
        if mascota_form.is_valid():
            mascota = mascota_form.save(commit=False)
            mascota.dueño = perfil  # Relacionar con el perfil del usuario
            mascota.save()
            messages.success(request, "Mascota creada exitosamente.")
            return redirect('usuario_exitoso')
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
                return redirect('home')  # Redirige a la vista principal
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

#@login_required  # Asegúrate de que solo los usuarios autenticados puedan acceder
def user_profile(request):
    # Aquí puedes agregar la lógica para obtener el perfil del usuario
    perfil = get_object_or_404(UserProfile, usuario=request.user)  # Suponiendo que tienes un modelo UserProfile

    return render(request, 'home/usuarios/perfil.html', {'perfil': perfil})