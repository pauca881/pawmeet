from django.urls import path
from .views import mascotas


urlpatterns = [
path('', mascotas, name='mascotas'),
]