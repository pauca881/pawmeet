from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from usuarios.models import UserProfile  # Asegúrate de que este modelo esté importado
from usuarios.forms import UserForm, UserProfileForm

def listar_usuarios(request):
    # Cambiado para usar el modelo de usuarios
    usuarios = User.objects.all()
    perfiles = UserProfile.objects.all()  # Si quieres mostrar los perfiles asociados
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios, 'perfiles': perfiles})

def crear_usuario(request):
    if request.method == 'POST':
        # Se incluye request.FILES para manejar archivos
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # Guardar el usuario
            usuario = user_form.save(commit=False)
            usuario.set_password(user_form.cleaned_data['password'])  # Encripta la contraseña
            usuario.save()

            # Guardar el perfil asociado al usuario
            perfil = profile_form.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

            # Redirigir a la lista de usuarios
            return redirect('listar_usuarios')
    else:
        # Formularios vacíos si es GET
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'crear_usuario.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def usuario_exitoso(request):
    return render(request, 'usuario_exitoso.html')
