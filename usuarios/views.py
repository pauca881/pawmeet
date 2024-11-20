from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from usuarios.models import UserProfile
from usuarios.forms import UserProfileCreationForm
from usuarios.forms import UserForm

def listar_usuarios(request):
    # Cambiado para usar el modelo de usuarios
    usuarios = User.objects.all()
    perfiles = UserProfile.objects.all()  # Si quieres mostrar los perfiles asociados
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios, 'perfiles': perfiles})

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

            # Redirigir a la vista para elegir crear mascota o ir al éxito
            return redirect('crear_mascota_opcion', usuario_id=usuario.id)
    else:
        user_form = UserForm()
        profile_form = UserProfileCreationForm()

    return render(request, 'crear_usuario.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def crear_mascota_opcion(request, usuario_id):
    return render(request, 'crear_mascota_opcion.html', {'usuario_id': usuario_id})



def crear_mascota(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    if request.method == 'POST':
        mascota_form = MascotaForm(request.POST, request.FILES)
        if mascota_form.is_valid():
            mascota = mascota_form.save(commit=False)
            mascota.usuario = usuario  # Relacionar con el usuario
            mascota.save()
            return redirect('usuario_exitoso')
    else:
        mascota_form = MascotaForm()

    return render(request, 'crear_mascota.html', {'mascota_form': mascota_form})


def usuario_exitoso(request):
    return render(request, 'usuario_exitoso.html')
