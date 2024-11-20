from django.urls import path, include
from .views import mascotas


urlpatterns = [
    path('', mascotas, name='mascotas')
]
