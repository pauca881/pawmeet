from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
# a

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():  # Si el formulario es válido, guarda los datos
            form.save()#polla
            # Redirige a una página de éxito o listado
            return redirect('usuario_exitoso')
        else:
            # Si el formulario no es válido (por ejemplo, por la validación de edad), se vuelve a mostrar con los errores
            return render(request, 'crear_usuario.html', {'form': form})
    else:
        form = UsuarioForm()  # Si es un GET, muestra el formulario vacío
    return render(request, 'crear_usuario.html', {'form': form})
