# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_mascota/<int:usuario_id>/', views.crear_mascota, name='crear_mascota'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),  # Asegúrate de que esto esté incluido
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]



# En desarrollo, servir archivos estáticos y de medios
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
