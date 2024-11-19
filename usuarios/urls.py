# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import listar_usuarios, crear_usuario, usuario_exitoso

urlpatterns = [
    # Aquí irían otras URLs de tu proyecto
    # ejemplo de cómo incluir URLs de una app
    path('', listar_usuarios, name='listar_usuarios'),
    path('crear-usuario/', crear_usuario, name='crear_usuario'),
    path('usuario_exitoso/', usuario_exitoso, name='usuario_exitoso'),
]

# En desarrollo, servir archivos estáticos y de medios
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
