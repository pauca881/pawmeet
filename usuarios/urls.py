# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_mascota_opcion/<int:usuario_id>/', views.crear_mascota_opcion, name='crear_mascota_opcion'),
    path('crear_mascota/<int:usuario_id>/', views.crear_mascota, name='crear_mascota'),
    path('usuario_exitoso/', views.usuario_exitoso, name='usuario_exitoso'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),  # Asegúrate de que esto esté incluido
]



# En desarrollo, servir archivos estáticos y de medios
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
