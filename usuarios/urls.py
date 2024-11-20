# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from usuarios.views import listar_usuarios, crear_usuario, usuario_exitoso, crear_mascota_opcion, crear_mascota

urlpatterns = [
    path('usuarios/crear/', crear_usuario, name='crear_usuario'),
    path('usuarios/crear/mascota_opcion/<int:usuario_id>/', crear_mascota_opcion, name='crear_mascota_opcion'),
    path('usuarios/crear/mascota/<int:usuario_id>/', crear_mascota, name='crear_mascota'),
    path('usuarios/exitoso/', usuario_exitoso, name='usuario_exitoso'),
]


# En desarrollo, servir archivos estáticos y de medios
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
