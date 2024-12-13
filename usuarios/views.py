from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from usuarios.models import UserProfile
from usuarios.forms import UserProfileCreationForm, UserForm, SeleccionarTipoUsuarioForm, RegistroProfesionalForm
from mascotas.forms import MascotaForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mascotas.models import Mascota

import logging

def listar_usuarios(request):
    usuarios = User.objects.all()  # Usuarios registrados
    perfiles = UserProfile.objects.all()  # Perfiles de usuario
    return render(request, 'listar_usuarios.html', {
        'usuarios': usuarios,
        'perfiles': perfiles
    })


"""
TERCER VIEWS PER TIPUS DE USUARI (he provat dos, el que esta sense comentar es l'inicial)
def crear_usuario(request):
    user_form = UserForm()
    profile_form = UserProfileCreationForm()
    profesional_form = RegistroProfesionalForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        tipo_usuario_form = SeleccionarTipoUsuarioForm(request.POST)

        if tipo_usuario_form.is_valid():
            tipo_usuario = tipo_usuario_form.cleaned_data['tipo_usuario']

            if tipo_usuario == 'mejor amigo de la mascota':
                profile_form = UserProfileCreationForm(request.POST)
                if user_form.is_valid() and profile_form.is_valid():
                    # Crear usuario y perfil normal
                    usuario = user_form.save(commit=False)
                    usuario.set_password(user_form.cleaned_data['password'])
                    usuario.save()

                    perfil = profile_form.save(commit=False)
                    perfil.usuario = usuario
                    perfil.save()

                    login(request, usuario)
                    messages.success(request, 'Usuario creado exitosamente.')
                    return redirect('crear_mascota', usuario_id=usuario.id)

            elif tipo_usuario == 'profesional':
                profesional_form = RegistroProfesionalForm(request.POST)
                if user_form.is_valid() and profesional_form.is_valid():
                    # Crear usuario y perfil profesional
                    usuario = user_form.save(commit=False)
                    usuario.set_password(user_form.cleaned_data['password'])
                    usuario.save()

                    profesional = profesional_form.save(commit=False)
                    profesional.usuario = usuario
                    profesional.save()

                    login(request, usuario)
                    messages.success(request, 'Usuario profesional creado exitosamente.')
                    return redirect('inicio')

    return render(request, 'crear_usuario.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profesional_form': profesional_form,
    })
    """

"""
SEGON VIEWS PER DOS TIPUS DE USUARI
def crear_usuario(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        tipo_usuario = request.POST.get('tipo_usuario')

        if tipo_usuario == 'dueño':
            profile_form = UserProfileCreationForm(request.POST, request.FILES)
        elif tipo_usuario == 'profesional':
            profile_form == RegistroProfesionalForm(request.POST, request.FILES)
        else: 
            messages.error(request, 'Tipo de usuario no valido.')
            return redirect('crear_usuario')
        
        if user_form.is_valid() and profile_form.is_valid():
            usuario = user_form.save(commit = False)
            usuario.set_password(user_form.cleaned_data['password'])
            usuario.save()

            user = authenticate(username = usuario.username, password = user_form.cleaned_data['password'])
            if user is not None:
                login(request, user)

            messages.success(request, 'Usuario creado exitosamente.')

            if tipo_usuario == 'dueño':
                return redirect('crear_mascota', usuario_id=usuario.id)
            elif tipo_usuario == 'profesional':
                return redirect('dashboard_profesional')
    else:
        user_form = UserForm()
        profile_form = None

    return render(request, 'crear_usuario.html', {
        'user_form' : user_form,
        'profile_form' : profile_form
    })

"""

#PRIMER VIEWS PER USUARI
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

            user = authenticate(username=usuario.username, password=user_form.cleaned_data['password'])
            if user is not None:
                login(request, user)

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
    

@login_required
def crear_mascota(request, usuario_id):
    perfil = get_object_or_404(UserProfile, usuario_id=usuario_id)
    if request.method == 'POST':
        mascota_form = MascotaForm(request.POST, request.FILES)

        if mascota_form.is_valid():
            mascota = mascota_form.save(commit=False)
            mascota.dueño = perfil
            mascota.save()
            messages.success(request, 'Mascota añadida.')
            return render(request, 'crear_mascota.html', {
                'mascota_form': mascota_form,
                'messages': messages.get_messages(request)
            })
        if not mascota_form.is_valid():
            logging.critical("error")
            logging.critical(mascota_form.errors)
            logging.critical("error_end")
    else:
        mascota_form = MascotaForm()

    return render(request, 'crear_mascota.html', {'mascota_form': mascota_form})

@login_required
def perfil(request):
    # Obtener las mascotas asociadas al usuario
    mascotas = Mascota.objects.filter(dueño=request.user.userprofile)  # Relación con el perfil del usuario
    return render(request, 'perfil.html', {'mascotas': mascotas})

@login_required
def editar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id, dueño=request.user.userprofile)  # Filtrar por usuario

    if request.method == 'POST':
        mascota_form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if mascota_form.is_valid():
            mascota_form.save()
            messages.success(request, 'Mascota actualizada correctamente.')
            return redirect('perfil')  # Redirigir al perfil después de guardar
    else:
        mascota_form = MascotaForm(instance=mascota)

    return render(request, 'editar_mascota.html', {'mascota_form': mascota_form})

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
    return redirect('login')  # Redirige a la página de login después del logout)


