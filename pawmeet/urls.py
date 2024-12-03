from django.contrib import admin
from django.urls import include, path
from home import urls  # Importamos la vista home desde la app home


urlpatterns = [
    path('admin/', admin.site.urls),
    # Ruta raíz, ahora apuntando a la vista home
    path('', include('home.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('mascotas/', include('mascotas.urls')),
    path('report/', include('lostpets.urls')),
    path('chatbot/', include('chatbot.urls')),

]
