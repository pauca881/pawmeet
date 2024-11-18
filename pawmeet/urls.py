from django.contrib import admin
from django.urls import include, path
from home import views  # Importamos la vista home desde la app home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, include('home.urls')), # Ruta raíz, ahora apuntando a la vista home
    path('usuarios/', include('usuarios.urls')),
]
