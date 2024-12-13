# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_mascota/<int:usuario_id>/', views.crear_mascota, name='crear_mascota'),
    path('perfil/', views.perfil, name='perfil'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('eliminar_cuenta/', views.eliminar_cuenta, name='eliminar_cuenta'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('editar_mascota/<int:mascota_id>/', views.editar_mascota, name='editar_mascota'),
]



# En desarrollo, servir archivos estáticos y de medios
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
