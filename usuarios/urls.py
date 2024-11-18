# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    # Aquí irían otras URLs de tu proyecto
    # ejemplo de cómo incluir URLs de una app
    path('usuarios/', include('usuarios.urls')),

    # Puedes agregar aquí más rutas que necesites para tu proyecto
]

# En desarrollo, servir archivos estáticos y de medios
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)