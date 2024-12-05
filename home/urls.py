from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('conectar/', views.conectar_view, name='conectar'),
    path('mascotas_cercanas/', views.ver_mascota_cercana_view, name='mascotas_cercanas'),
    path('list_mascotas/', views.list_mascotas_view, name='list_mascotas'),
    path('meetups/', views.eventos_view, name='eventos'),
    path('home/', views.home_view, name='home')
]
