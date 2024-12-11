from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('conectar/', views.conectar_view, name='conectar'),
    path('mascotas_cercanas/', views.ver_mascota_cercana_view, name='mascotas_cercanas'),
    path('meetups/', views.eventos_view, name='eventos'),
    path('agregar_amigo/', views.agregar_amigo, name='agregar_amigo'),
    path('listar_amigos/', views.listar_amigos, name='listar_amigos'),

]
