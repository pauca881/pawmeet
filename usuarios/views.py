from django.shortcuts import render, redirect
from usuarios.forms import UserForm, UserProfileForm

def listar_usuarios(request):
    usuarios = UserForm.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Guardar el usuario
            usuario = user_form.save()
            usuario.set_password(user_form.cleaned_data['password'])
            usuario.save()

            # Guardar el perfil asociado al usuario
            perfil = profile_form.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

            return redirect('listar_usuarios')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'crear_usuario.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def usuario_exitoso(request):
    return render(request, 'usuario_exitoso.html')
