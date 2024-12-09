from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('mascotas/', include('mascotas.urls')),
    path('report/', include('lostpets.urls')),
    path('petadvisor/', include('petadvisor.urls')),
    path('chatbot/', include('chatbot.urls')),
]
